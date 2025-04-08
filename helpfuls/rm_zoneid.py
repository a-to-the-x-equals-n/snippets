from pathlib import Path

PR = f'\033[38;5;129m'
RD = f'\033[91m'
MG = f'\033[95m'
YW = f'\033[93m'
GR = f'\033[92m'
_X = f'\033[0m'

def delete_zone_identifier_files(directory: str | Path) -> int:
    '''
    Recursively deletes all files ending with 'Zone.Identifier' in the given directory and its subdirectories.
    
    Args:
    -----
        directory (str | Path): Path to search (relative or absolute)

    Returns:
    --------
        int: Number of files successfully deleted
    '''
    dir = Path(directory).resolve()
    deleted = 0
    
    print(f'\n{YW}[RESOLVED]{_X}: {PR}{directory}{_X} to {MG}{dir}{_X}.')
    print(f'{YW}[SEARCHING]{_X}: {PR}*Zone.Identifier{_X} in {MG}{dir}{_X}.')

    for fpath in dir.rglob('*Zone.Identifier'):
        try:
            fpath.unlink()
            print(f'{YW}[DELETED]{_X}: {PR}{fpath}{_X}')
            deleted += 1
        except PermissionError:
            print(f'{RD}[PERMISSION DENIED]{_X}: {PR}{fpath}{_X}.')
        except Exception as e:
            print(f'{RD}[ERROR]{_X} {PR}{fpath}: {YW}{str(e)}{_X}.')
    
    return deleted



if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 2:
        print(f'{YW}[USAGE]{_X}: python rm_identifier.py <directory>')
        sys.exit(1)
    
    dir = Path(sys.argv[1])
    
    if not dir.is_dir():
        print(f"{RD}[ERROR]{_X}: '{MG}{dir}{_X}' is not a valid directory.")
        sys.exit(1)
    
    if (ct := delete_zone_identifier_files(dir)) == 0:
        print(f'{GR}[SUCCESS]{_X}: No files found with {PR}*Zone.Identifier{_X}.')
    else:
        print(f'{GR}[SUCCESS]{_X}: {MG}{ct}{_X} files delted with {PR}*Zone.Identifier{_X}.')
