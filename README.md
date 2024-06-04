# DarkReign
DarkReignAsciiNameGenerator2 is a tool for customizing player names in Dark Reign - The Future of War. It allows users to create ASCII-based names and updates the TACTICS.CFG file for use in-game, adding a personalized touch to the gaming experience.

# DarkReignAsciiNameGenerator2

DarkReignAsciiNameGenerator2 is a simple Python application that allows users to generate ASCII names for the legacy video game Dark Reign - The Future of War. The app modifies the player name in the `TACTICS.CFG` file to include ASCII characters.

## Features

- Easy-to-use GUI for generating ASCII names
- Supports ASCII characters from A to Z and numbers
- Dynamically updates the player name in the `TACTICS.CFG` file

## Prerequisites

- Python 3.6 or higher
- Required Python packages:
  - cx_Freeze (for creating an executable)
  - os

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/DarkReignAsciiNameGenerator2.git
    cd DarkReignAsciiNameGenerator2
    ```

2. Install the required packages:
    ```bash
    pip install cx_Freeze os
    ```

## Usage

1. Run the application:
    ```bash
    python dark_reign_name_generator_grid.py
    ```

2. Use the GUI to generate your desired ASCII name and save it to the `TACTICS.CFG` file.

## Building the Executable

To create a standalone executable for the application:

1. Create a `setup.py` file with the following content:
    ```python
    from cx_Freeze import setup, Executable

    base = None

    executables = [Executable("dark_reign_name_generator_grid.py", base=base)]

    packages = ["idna", "os"]
    options = {
        'build_exe': {
            'packages': packages,
        },
    }

    setup(
        name="DarkReignAsciiNameGenerator2",
        options=options,
        version="1.0",
        description="Dark Reign Ascii Name Generator",
        executables=executables
    )
    ```

2. Run the following command to build the executable:
    ```bash
    python setup.py build
    ```

3. The executable will be created in the `build` directory.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or feedback, feel free to reach out to me at your.email@example.com.

