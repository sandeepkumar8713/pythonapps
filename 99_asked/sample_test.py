from sample_2 import solve, parse_input, take_one_step, change_direction

test_cases = [
  {
    "input": "10,20/2,3,N/FFRF",
    "output": "3,5,E"
  },
  {
    "input": "13,21/0,0,N/FFFFF",
    "output": "0,5,N"
  },
  {
    "input": "13,21/0,0,E/FFFFF",
    "output": "5,0,E"
  },
  {
    "input": "10,20/2,3,N/RFFFFLFFFFFF",
    "output": "6,9,N"
  },
  {
    "input": "20,20/18,6,E/FFFFRFFFFFF",
    "output": "20,0,S"
  },
  {
    "input": "20,20/2,0,W/FFFF",
    "output": "0,0,W"
  }
]

def test_parse_input():
    inp_str = "10,20/2,3,N/FFRF"
    result = parse_input(inp_str)
    assert result["grid_size"] == (10, 20)
    assert result['initial_position'] == (2, 3, 'N')
    assert result['commands'] == 'FFRF'


def test_first_step():
  grid_size = (10, 20)
  current_position = (2, 3, 'N')

  new_position = (2, 4, 'N')
  assert new_position == take_one_step(current_position, grid_size)

def test_change_direction():
  current_direction = 'N'
  command = 'L'

  assert 'W' == change_direction(current_direction, command)

def test_parsing_of_input():
    for case in test_cases:
        i = case["input"]
        o = case["output"]
        assert solve(i) == o
