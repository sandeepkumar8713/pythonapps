

def parse_input(inp_str):
    result = dict()
    inp_list = inp_str.split("/")
    if len(inp_list) != 3:
        raise Exception("Invalid Input")

    grid_size_str = inp_list[0]
    grid_size_list = grid_size_str.split(",")
    if len(grid_size_list) != 2:
        raise Exception("Invalid grid list input")
    try:
        X = int(grid_size_list[0])
        Y = int(grid_size_list[1])
        result['grid_size'] = (X, Y)
    except Exception as e:
        raise Exception("Invalid grid list input")

    initial_position_str = inp_list[1]
    initial_position_list = initial_position_str.split(",")
    if len(initial_position_list) != 3:
        raise Exception("Invalid initial position list input")
    try:
        x = int(initial_position_list[0])
        y = int(initial_position_list[1])
        d = initial_position_list[2]
        if d not in ['N', 'E', 'W', 'S']:
            raise Exception("Invalid direction")
        result['initial_position'] = (x, y, d)
    except Exception as e:
        raise Exception(str(e))

    commands_str = inp_list[2]
    result['commands'] = commands_str
    return result

def change_direction(current_direction, command):
    direction_list = ['N', 'E', 'S', 'W']
    current_direction_index = direction_list.index(current_direction)

    if command == 'L':
        next_direction = (current_direction_index - 1) % 4
    if command == 'R':
        next_direction = (current_direction_index + 1) % 4

    return direction_list[next_direction]

def take_one_step(current_position, grid_size):
    direction_list = ['N', 'E', 'S', 'W']
    next_step = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    x = current_position[0]
    y = current_position[1]

    direction_index = direction_list.index(current_position[2])
    next_step_delta = next_step[direction_index]
    next_x = x + next_step_delta[0]
    next_y = y + next_step_delta[1]

    if 0 <= next_x <= grid_size[0] and 0 <= next_y <= grid_size[1]:
        return (next_x, next_y, current_position[2])

    return current_position

def solve(inp_str):
    input_dict = parse_input(inp_str)
    grid_size = input_dict["grid_size"]
    initial_position = input_dict['initial_position']
    commands = input_dict['commands']

    current_position = initial_position
    for command in commands:
        if command == 'F':
            current_position = take_one_step(current_position, grid_size)
        elif command in ['R', 'L']:
            new_direction = change_direction(current_position[2], command)
            current_position = (current_position[0], current_position[1], new_direction)

    result_list = []
    for item in current_position:
        result_list.append(str(item))

    return ",".join(result_list)