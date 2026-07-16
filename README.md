# File Organizer

A Python-based File Organizer that automatically sorts files into categorized folders based on their file extensions.

This project was built to practice Python fundamentals while learning real-world software development concepts such as modular programming, GUI development, JSON configuration, and filesystem automation.

---

## Features

- Automatically organizes files into categories
- Simple GUI built with Tkinter
- Configurable categories using `config.json`
- Automatically creates folders if they don't exist
- Prevents overwriting duplicate files
    - `photo.jpg`
    - `photo_1.jpg`
    - `photo_2.jpg`
- Optional real-time monitoring using Watchdog
- Modular project structure
- Uses `pathlib` for modern path handling
- Uses `shutil` for moving files

---

## Categories

Current supported categories include:

- Applications
- Images
- Documents
- Videos
- Audio
- Archives/Others

New categories and extensions can be added by simply editing `config.json`.

Example:

```json
{
    "ebooks": [".epub", ".mobi"]
}
```

No changes to the Python code are required.

---

## Technologies Used

- Python
- pathlib
- shutil
- json
- tkinter
- watchdog

---

## Project Structure

```
FileOrganizer/
│
├── organizer.py
├── organizer_GUI.py
├── organizer_watchdog.py
├── config.json
└── README.md
```

---

## Concepts Practiced

This project helped me learn:

- File handling
- Directory traversal
- Modern path manipulation with pathlib
- Modular programming
- Function decomposition
- JSON configuration files
- GUI development using Tkinter
- Event-driven programming using Watchdog
- Duplicate file handling
- Input validation
- Code organization

---

## Future Improvements

- Better logging
- Drag & Drop support
- Progress bar
- Multi-threading
- File history
- Undo feature
- Executable (.exe) release
- Custom themes

---

## How to Run

Install the required dependency:

```bash
pip install watchdog
```

Run the GUI:

```bash
python organizer_GUI.py
```

Or use the real-time organizer:

```bash
python organizer_watchdog.py
```

---

## Author

**Parth Lohani**

Built while learning Python and software development from scratch.
