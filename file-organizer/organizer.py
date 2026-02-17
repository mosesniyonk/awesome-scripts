import os
import shutil
import sys
from pathlib import Path

# Mapping of file extensions to folder names
EXTENSION_MAP = {
    # Documents
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.doc': 'Documents',
    '.txt': 'Documents',
    '.csv': 'Documents',
    '.xlsx': 'Documents',
    '.pptx': 'Documents',
    '.md': 'Documents',
    # Images
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.svg': 'Images',
    '.webp': 'Images',
    # Audio
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.flac': 'Audio',
    # Video
    '.mp4': 'Video',
    '.mkv': 'Video',
    '.mov': 'Video',
    # Archives
    '.zip': 'Archives',
    '.tar': 'Archives',
    '.gz': 'Archives',
    '.rar': 'Archives',
    '.7z': 'Archives',
    # Scripts/Code
    '.py': 'Scripts',
    '.js': 'Scripts',
    '.sh': 'Scripts',
    '.json': 'Data'
}

def organize_folder(target_dir):
    path = Path(target_dir)
    
    if not path.exists():
        print(f"Error: {target_dir} does not exist.")
        return

    print(f"Organizing files in: {path.absolute()}")

    for item in path.iterdir():
        # Skip directories
        if item.is_dir():
            continue
        
        # Skip the script itself if it's in the same folder
        if item.name == __file__:
            continue

        ext = item.suffix.lower()
        folder_name = EXTENSION_MAP.get(ext, 'Others')

        dest_folder = path / folder_name
        dest_folder.mkdir(exist_ok=True)

        dest_path = dest_folder / item.name
        
        # Handle filename collisions
        if dest_path.exists():
            count = 1
            while dest_path.exists():
                new_name = f"{item.stem}_{count}{item.suffix}"
                dest_path = dest_folder / new_name
                count += 1
        
        print(f"Moving: {item.name} -> {folder_name}/")
        shutil.move(str(item), str(dest_path))

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    organize_folder(target)
    print("Done!")
