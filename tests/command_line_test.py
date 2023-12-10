# tests/line_test.py (or test_command_line.py)

import sys
from pathlib import Path

# Append the project root directory to sys.path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from command_line import parse_args

def test_cli():
    test_url = 'https://svelte.dev/docs/introduction'
    args = parse_args([test_url])
    assert args.url == test_url
