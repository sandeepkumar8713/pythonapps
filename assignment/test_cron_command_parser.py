from cron_command_parser import (
    ParserType,
    ParserFactory,
    InvalidInputException,
    InvalidTimeRangeException,
    parse_cron_command,
    InvalidFieldCountException)
import pytest


def test_minute_parser_with_valid_input():
    parser = ParserFactory.get_parser(ParserType.MINUTE)
    result = parser.parse('*/15')
    assert result == [0, 15, 30, 45]


def test_minute_parser_with_multiple_ranges():
    parser = ParserFactory.get_parser(ParserType.MINUTE)
    result = parser.parse('*/5,1-4,10/4')
    assert result == [0, 1, 2, 3, 4, 5, 10, 14, 15, 18, 20, 22, 25, 26, 30, 34, 35, 38, 40, 42, 45, 46, 50, 54, 55, 58]


def test_minute_parser_with_non_sorted_ranges():
    parser = ParserFactory.get_parser(ParserType.MINUTE)
    result = parser.parse('23,0-7')
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 23]


def test_minute_parser_to_run_only_during_given_range_with_skip():
    parser = ParserFactory.get_parser(ParserType.MINUTE)
    result = parser.parse('10-20/6')
    assert result == [10, 16]


def test_minute_parser_with_invalid_range():
    parser = ParserFactory.get_parser(ParserType.MINUTE)
    with pytest.raises(InvalidTimeRangeException, match="Invalid time range for 'minute' field"):
        parser.parse('20-10')


def test_minute_parser_with_invalid_input():
    parser = ParserFactory.get_parser(ParserType.MINUTE)
    with pytest.raises(InvalidInputException, match="Invalid input for 'minute' field"):
        parser.parse('ab12')


def test_minute_parser_with_invalid_skip_interval():
    parser = ParserFactory.get_parser(ParserType.MINUTE)
    with pytest.raises(InvalidInputException, match="Invalid input for 'minute' field"):
        parser.parse('*/-56')


def test_minute_parser_with_invalid_range_for_skip():
    parser = ParserFactory.get_parser(ParserType.MINUTE)
    with pytest.raises(InvalidTimeRangeException, match="Invalid time range for 'minute' field"):
        parser.parse('-56/1')


def test_hour_parser_with_invalid_interval_in_skip():
    parser = ParserFactory.get_parser(ParserType.HOUR)
    with pytest.raises(InvalidInputException, match="Invalid input for 'hour' field"):
        parser.parse('*/0')


def test_day_parser_with_prefix_zero():
    parser = ParserFactory.get_parser(ParserType.DAY_OF_MONTH)
    result = parser.parse('04')
    assert result == [4]


def test_day_of_month_parser_with_invalid_range():
    parser = ParserFactory.get_parser(ParserType.DAY_OF_MONTH)
    with pytest.raises(InvalidTimeRangeException, match="Invalid time range for 'day of month' field"):
        parser.parse('a-5')


def test_month_parser_with_valid_input():
    parser = ParserFactory.get_parser(ParserType.MONTH)
    result = parser.parse('10,3')
    assert result == [3, 10]


def test_day_of_week_parser_with_double_zero():
    parser = ParserFactory.get_parser(ParserType.DAY_OF_WEEK)
    result = parser.parse('00')
    assert result == [0]


def test_day_of_week_parser_with_wild_card():
    parser = ParserFactory.get_parser(ParserType.DAY_OF_WEEK)
    result = parser.parse('*')
    assert result == [0, 1, 2, 3, 4, 5, 6]


def test_day_of_week_parser_with_invalid_range():
    parser = ParserFactory.get_parser(ParserType.DAY_OF_WEEK)
    with pytest.raises(InvalidTimeRangeException, match="Invalid time range for 'day of week' field"):
        parser.parse('5-10')


def test_parse_cron_command_with_invalid_numbers_of_field():
    with pytest.raises(InvalidFieldCountException, match="Input string should have 6 fields"):
        parse_cron_command("*/15 0")


def test_parse_cron_command_with_valid_input():
    str_output_list = parse_cron_command("*/15 0 1,15 * 1-5 /usr/bin/find")
    assert str_output_list[0] == "minute        0 15 30 45"
    assert str_output_list[1] == "hour          0"
    assert str_output_list[2] == "day of month  1 15"
    assert str_output_list[3] == "month         1 2 3 4 5 6 7 8 9 10 11 12"
    assert str_output_list[4] == "day of week   1 2 3 4 5"
    assert str_output_list[5] == "command       /usr/bin/find"


def test_parse_cron_command_with_all_star():
    str_output_list = parse_cron_command("* * * * * /usr/bin/find")
    assert str_output_list[
               0] == "minute        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59"
    assert str_output_list[1] == "hour          0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23"
    assert str_output_list[
               2] == "day of month  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31"
    assert str_output_list[3] == "month         1 2 3 4 5 6 7 8 9 10 11 12"
    assert str_output_list[4] == "day of week   0 1 2 3 4 5 6"
    assert str_output_list[5] == "command       /usr/bin/find"


def test_parse_cron_command_with_multiple_fields_being_invalid():
    str_output_list = parse_cron_command("*/0 20-20 1,45 * a /usr/bin/find")
    assert len(str_output_list) == 4
    assert str_output_list[0] == "Exception occurred while parsing field [*/0] : Invalid input for 'minute' field"
    assert str_output_list[1] == "Exception occurred while parsing field [20-20] : Invalid time range for 'hour' field"
    assert str_output_list[
               2] == "Exception occurred while parsing field [1,45] : Invalid input for 'day of month' field"
    assert str_output_list[3] == "Exception occurred while parsing field [a] : Invalid input for 'day of week' field"
