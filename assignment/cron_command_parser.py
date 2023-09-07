import sys
import re
import abc

from enum import Enum


def create_exception_message(msg_prefix, field):
    field_name = "'" + field.value.lower().replace("_", " ") + "'"
    return msg_prefix + field_name + " field"


class InvalidInputException(Exception):
    def __init__(self, field):
        message = create_exception_message("Invalid input for ", field)
        super().__init__(message)


class InvalidTimeRangeException(Exception):
    def __init__(self, field):
        message = create_exception_message("Invalid time range for ", field)
        super().__init__(message)


class InvalidFieldCountException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ParserType(Enum):
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY_OF_MONTH = "DAY_OF_MONTH"
    MONTH = "MONTH"
    DAY_OF_WEEK = "DAY_OF_WEEK"
    YEAR = "YEAR"
    COMMAND = "COMMAND"


class Parser(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def parse(self, sub_str):
        pass


class TimeParser(Parser):
    def __init__(self, atom_reg_exp, lower_limit, upper_limit, field):
        self.atom_reg_exp = atom_reg_exp
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.field = field

    def parse_star(self):
        result = set()
        for value in range(self.lower_limit, self.upper_limit + 1):
            result.add(value)
        return result

    def convert_atom_to_time(self, atom):
        exp = '^' + self.atom_reg_exp + '$'
        regexp = re.compile(exp)
        matched = regexp.search(atom)
        if matched:
            return int(atom)

        raise InvalidInputException(self.field)

    def parse_division(self, atom):
        subatomic = atom.split('/')
        result = set()
        sub_result = self.find_range_from_atom(subatomic[0])
        interval = self.convert_atom_to_time(subatomic[1])

        sorted_list = sorted(list(sub_result))
        if len(sorted_list) == 0 or interval == 0:
            raise InvalidInputException(self.field)

        start = sorted_list[0]
        if len(sorted_list) == 1:
            end = self.upper_limit
        else:
            end = sorted_list[-1]

        while start <= end:
            result.add(start)
            start += interval

        return result

    def parse_hyphen(self, atom):
        sub_result = set()
        exp = '^' + self.atom_reg_exp + '-' + self.atom_reg_exp + '$'
        regexp_1 = re.compile(exp)
        matched_1 = regexp_1.search(atom)
        if matched_1:
            checkout_strs = atom.split("-")
            start = int(checkout_strs[0])
            end = int(checkout_strs[1])

            if start >= end:
                raise InvalidTimeRangeException(self.field)

            for value in range(start, end + 1):
                sub_result.add(int(value))
        else:
            raise InvalidTimeRangeException(self.field)

        return sub_result

    def find_range_from_atom(self, atom):
        result = set()
        if '*' == atom:
            result = self.parse_star()
        elif '/' in atom:
            sub_result = self.parse_division(atom)
            result = result.union(sub_result)
        elif '-' in atom:
            sub_result = self.parse_hyphen(atom)
            result = result.union(sub_result)
        else:
            sub_result = self.convert_atom_to_time(atom)
            result.add(sub_result)

        return result

    def parse_atoms(self, atoms):
        result = set()
        for atom in atoms:
            sub_result = self.find_range_from_atom(atom)
            result = result.union(sub_result)

        return sorted(list(result))

    def parse(self, sub_str):
        atoms = sub_str.split(",")
        return self.parse_atoms(atoms)


class CommandParser(Parser):
    def __init__(self, label):
        self.label = label

    def parse(self, sub_str):
        print(sub_str)
        return [sub_str]


class ParserFactory:
    @staticmethod
    def get_parser(parser_type):
        parser_obj = None
        if parser_type == ParserType.MINUTE:
            parser_obj = TimeParser(atom_reg_exp='(0?[0-9]|[1-5][0-9])',
                                    lower_limit=0,
                                    upper_limit=59,
                                    field=parser_type
                                    )
        elif parser_type == ParserType.HOUR:
            parser_obj = TimeParser(atom_reg_exp='(0?[0-9]|[1][0-9]|[2][0-3])',
                                    lower_limit=0,
                                    upper_limit=23,
                                    field=parser_type
                                    )
        elif parser_type == ParserType.DAY_OF_MONTH:
            parser_obj = TimeParser(atom_reg_exp='(0?[1-9]|[12][0-9]|[3][0-1])',
                                    lower_limit=1,
                                    upper_limit=31,
                                    field=parser_type
                                    )
        elif parser_type == ParserType.MONTH:
            parser_obj = TimeParser(atom_reg_exp='(0?[1-9]|[1][0-2])',
                                    lower_limit=1,
                                    upper_limit=12,
                                    field=parser_type
                                    )
        elif parser_type == ParserType.DAY_OF_WEEK:
            parser_obj = TimeParser(atom_reg_exp='(0?[0-6])',
                                    lower_limit=0,
                                    upper_limit=6,
                                    field=parser_type
                                    )
        elif parser_type == ParserType.YEAR:
            parser_obj = TimeParser(atom_reg_exp='([2][0-9][0-9][0-9]|3000)',
                                    lower_limit=2000,
                                    upper_limit=3000,
                                    field=parser_type
                                    )
        elif parser_type == ParserType.COMMAND:
            parser_obj = CommandParser(label=parser_type)
        return parser_obj


class Parsed:
    def __init__(self, label, result_list):
        self.label = label
        self.result_list = result_list

    def get_output_str(self):
        output_label = [" "] * 14
        label_value = self.label.value.lower().replace("_", " ")
        for i in range(len(label_value)):
            output_label[i] = label_value[i]

        result_str_list = []
        for result in self.result_list:
            #if self.label.value == "COMMAND":
            result_str_list.append(str(result))


        result_str = " ".join(result_str_list)
        output_label_str = "".join(output_label)
        return output_label_str + result_str


def parse_cron_command(inp_str):
    sub_strs = inp_str.split(" ")

    year_atom = sub_strs[5]
    parser = ParserFactory.get_parser(ParserType.YEAR)
    sixth_is_year = False
    try:
        parser.parse(year_atom)
        sixth_is_year = True
    except Exception as e:
        sixth_is_year = False

    print (sixth_is_year)
    field_len = 6
    time_char_index = 5
    parser_types = [ParserType.MINUTE, ParserType.HOUR, ParserType.DAY_OF_MONTH,
                    ParserType.MONTH, ParserType.DAY_OF_WEEK]

    if sixth_is_year:
        time_char_index += 1
        field_len += 1
        parser_types.append(ParserType.YEAR)

    parser_types.append(ParserType.COMMAND)

    sub_strs_new = sub_strs[:time_char_index]
    combined_time = " ".join(sub_strs_new)
    last_index = len(combined_time)
    last_command = inp_str[last_index:]
    combined_command = "".join(last_command)
    combined_command = combined_command.lstrip(" ")
    print (combined_command)

    sub_strs_new.append(combined_command)

    print (sub_strs_new)

    if len(sub_strs_new) < field_len:
        raise InvalidFieldCountException(f"Input string should have {field_len} fields")


    parsed_list = []
    error_list = []

    for i in range(len(sub_strs_new)):
        try:
            parser = ParserFactory.get_parser(parser_types[i])
            result = parser.parse(sub_strs_new[i])
            parsed_list.append(Parsed(parser_types[i], result))
        except Exception as e:
            error_list.append("Exception occurred while parsing field [" + sub_strs_new[i] + "] : " + str(e))

    if len(error_list) >= 1:
        return error_list

    result_list = []
    for parsed in parsed_list:
        result_list.append(parsed.get_output_str())
    return result_list


def parse_and_print_cron_command(inp_str):
    try:
        str_output_list = parse_cron_command(inp_str)
        for item in str_output_list:
            print(item)
    except Exception as e:
        print("Exception occurred while parsing input string : " + str(e))


if __name__ == "__main__":
    n = len(sys.argv)
    if n == 2:
        parse_and_print_cron_command(sys.argv[1])
    else:
        print("Incorrect input argument")

    # parse_and_print_cron_command("*/15 0 1,15 * 1-5 /usr/bin/find")
    # python cron_command_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"

    # parse_and_print_cron_command("*/15 0 1,15 * 1-5 /usr/bin/find -v foo")
    # parse_and_print_cron_command("*/15 0 1,15 * 1-5 /usr/bin/find -v 'Multiple   spaces'")

    parse_and_print_cron_command("*/15 0 1,15 * 1-5 2023-2025 /usr/bin/find")

    # */15 0 1,15 * FRI-MON /usr/bin/find
    # 0-6
    # MON-SAT
    # FRI-MON
    # {'MON' : 1, 'TUE' : 2}
