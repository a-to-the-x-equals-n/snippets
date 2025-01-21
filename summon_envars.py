import os
from dotenv import load_dotenv
from pathlib import Path


def get_envars(*args: list[str]) -> list[str] | str:
    try:
        # elegant pathing to current workspace
        dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
        env = dir / ".env"
        load_dotenv(env) # "cache" .env file
    except Exception as e:
        print(f'Error opening .env file: {str(e)}')

    # returns the requested environment variables as a list or a string
    return [os.getenv(arg) for arg in args] if len(args) > 1 else os.getenv(args[0])