

# example import: from colors import red, blue, yellow

# ANSI color codes
_COLORS = {

    # foreground Colors
    'black': '\033[30m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'gray': '\033[90m',
    'light_red': '\033[31m',
    'light_green': '\033[32m',
    'light_yellow': '\033[33m',
    'light_blue': '\033[34m',
    'light_magenta': '\033[35m',
    'light_cyan': '\033[36m',

    # background Colors
    'bg_black': '\033[40m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m',

    # text Styles
    'bold': '\033[1m',
    'underline': '\033[4m',
    'reversed': '\033[7m',
    'dim': '\033[2m',
    
    # reset
    'reset': '\033[0m'
}

# generate color functions dynamically
for color, code in _COLORS.items():
    if color != 'reset':
        globals()[color] = lambda text, code = code: f"{code}{text}{_COLORS['reset']}"

__all__ = list(_COLORS.keys())  # controls what `from colors import *` brings in
