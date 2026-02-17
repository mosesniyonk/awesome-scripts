# File Organizer Agent

## Goal

Automatically organize files in a specified directory into categorized subfolders based on their file extensions (e.g., Images, Documents, Audio, Video, etc.).

## Pre-requisites

- Python 3.x
- Standard library modules (`os`, `shutil`, `pathlib`) - no external dependencies required.

## Usage

Run the script from the terminal, optionally providing the target directory as an argument:

```bash
python organizer.py /path/to/directory
```

If no directory is provided, it defaults to the current working directory.

## Maintenance

- The script logs its actions to the console.
- It does not overwrite files with the same name; instead, it appends a number if a collision occurs.
- You can customize the `EXTENSION_MAP` in `organizer.py` to add or change categories.
