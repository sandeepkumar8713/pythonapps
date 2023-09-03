# Corn Command Parser

## Problem Statement

Write a command line application or script which parses a cron string and expands each field  to show the times at 
which it will run. You may use whichever language you feel most comfortable with.

You should only consider the standard cron format with five time fields (minute, hour, day of  month, month, and 
day of week) plus a command, and you do not need to handle the special time strings such as "@yearly". The input will
be on a single line.

## Prerequisite

Following script requires python 3.6+ installed on the system with following packages installed.
1. pytest

We can install the package using following command.

```shell
python -m pip install pytest
```

## Execution Command

Command to execute the script is as follows from a shell prompt. It takes input from command line as a single string.

```shell
python cron_command_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```

Output of above command is as follows
```shell
minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
```

## Input format is as follows

The crontab command syntax has six fields separated by space where the first five represent the time to run the task
and the last one is for the command. 

1. minute (holds a value between 0-59)
2. hour (holds value between 0-23)
3. day of month (holds value between 1-31)
4. month (holds a value between 1-12)
5. day of week (holds a value between 0-6)
6. Command

## Testing

To run unit test cases we can execute following command:

```shell
pytest test_cron_command_parser.py
```
