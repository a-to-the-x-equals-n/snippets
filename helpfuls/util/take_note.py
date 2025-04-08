from typing import Callable
import os

class Notes:
    """
    A singleton class for storing and retrieving function notes dynamically.

    This class ensures that all instances share the same set of notes
    by using the singleton pattern. Notes are stored as key-value pairs,
    where the function name is the key and its corresponding note is the value.

    Attributes:
    -----------
    _instance : Notes | None
        The singleton instance of the Notes class.
    _notes : Dict[str, str]
        A dictionary storing function names as keys and their corresponding notes as values.
    """

    _instance: "Notes | None" = None
    _dir_path = os.path.join(os.getcwd(), "Notes")  # Default directory

    def __new__(cls, file: str) -> "Notes":
        """
        Implements the singleton pattern to ensure only one instance of Notes exists.

        Returns:
        --------
        Notes:
            The singleton instance of the Notes class.
        """

        if cls._instance is None:
            cls._instance = super(Notes, cls).__new__(cls)
            cls._instance._notes = {}
            cls._instance._file_path = os.path.join(cls._dir_path, file)
            cls._instance._load()  # Load notes when initializing
        return cls._instance

    def add(self, func_name: str, note: str) -> None:
        """
            Adds a note for a given function.

            Parameters:
            -----------
            func_name : str
                The name of the function for which the note is being added.
            note : str
                The note or docstring associated with the function.
        """
        self._notes[func_name] = note

    def append(self, func_name: str, note: str) -> None:
        """
        Appends additional information to an existing function note.
        
        If the function does not already have a note, a new note is created.

        Parameters:
        -----------
        func_name : str
            The name of the function.
        note : str
            The text to append to the existing note.
        """
        if func_name in self._notes:
            self._notes[func_name] += f"\n{note}"  # Append with a newline for readability
        else:
            self._notes[func_name] = note  # If no note exists, create one

    def update(self, func_name: str, note: str) -> None:
        """
        Replaces an existing function note with a new one.

        If the function does not have a note, a warning is printed.

        Parameters:
        -----------
        func_name : str
            The name of the function.
        note : str
            The new note to replace the old one.
        """
        if func_name in self._notes:
            self._notes[func_name] = note  # Replace existing note
        else:
            print(f"⚠️ No existing note for '{func_name}'. Use `add_note` instead.")

    def save(self) -> None:
            """Saves all notes to a text file in the 'Note' directory."""
            os.makedirs(self._dir_path, exist_ok=True)  # ✅ Create directory if missing
            with open(self._file_path, "w", encoding="utf-8") as f:
                for func_name, note in self._notes.items():
                    f.write(f"{func_name}:::{note}\n")  # Custom delimiter

    def _load(self) -> None:
        """Loads notes from the saved text file."""
        if not os.path.exists(self._file_path):
            return  # No file yet, skip loading

        with open(self._file_path, "r", encoding="utf-8") as f:
            for line in f:
                if ":::" in line:
                    func_name, note = line.strip().split(":::", 1)
                    self._notes[func_name] = note

    def __getattr__(self, func_name: str) -> Callable[[], None]:
        """
            Retrieves the note for a function dynamically.

            If the function name exists in the stored notes, returns a lambda function
            that prints the note when called. Otherwise, raises an AttributeError.

            Parameters:
            -----------
            func_name : str
                The name of the function whose note is being retrieved.

            Returns:
            --------
            Callable[[], None]:
                A lambda function that prints the note when executed.

            Raises:
            -------
            AttributeError:
                If no note is found for the given function name.
        """
        if func_name in self._notes:
            return lambda: print(self._notes[func_name])
        else:
            def error_message() -> None:
                print(f"\n⚠️ No note found for function '{func_name}'. Please add a note before calling it.")
            return error_message  # instead of raising an error, return a function that prints a warning


if __name__ == "__main__":

    # Create a Notes instance with a custom filename
    notes = Notes("my_notes.txt")

    # Add and retrieve a note
    notes.add_note("example_func", "This function demonstrates the Notes class.")
    notes.example_func()  # Output: This function demonstrates the Notes class.

    # Append additional details
    notes.append_note("example_func", "It also supports saving with custom filenames.")
    notes.example_func()
    # Output:
    # This function demonstrates the Notes class.
    # It also supports saving with custom filenames.

    # Replace the note
    notes.replace_note("example_func", "This function note has been updated.")
    notes.example_func()  # Output: This function note has been updated.

    # Restart the program and reload from the custom file
    notes2 = Notes("my_notes.txt")  # Uses the same file
    notes2.example_func()  # Notes persist across program runs!

    notes.save()


    

