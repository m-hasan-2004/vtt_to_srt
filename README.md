# VTT to SRT Converter

This repository contains a Python script that converts `.vtt` (WebVTT) subtitle files to `.srt` (SubRip Subtitle) format. This is particularly useful for users who need to convert subtitle files from one format to another for compatibility with various media players or platforms.

## Features

- **Batch Conversion:** The script can convert multiple `.vtt` files in a directory to `.srt` format with a single command.
- **Timestamp Conversion:** Automatically converts timestamp format from VTT (e.g., `00:01:02.500`) to SRT (e.g., `00:01:02,500`).
- **Maintains Subtitle Structure:** The script preserves the original structure of the subtitles, ensuring that they remain in sync with the video.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository:**

    ```bash
    git clone git@github.com:m-hasan-2004/vtt_to_srt.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd vtt-to-srt
    ```

3. **(Optional) Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install any required dependencies:**

    This script does not require any external Python packages.

## Usage

1. **Place your `.vtt` files** in a directory on your system.

2. **Edit the `main()` function** in the `main.py` file to specify the path to your directory:

    ```python
    directory = r"path/to/your/directory"
    ```

3. **Change The Permissions Using Terminal**
    ```bash
    sudo chmod +x main.py
    ```

4. **Run the script:**

    ```bash
    python main.py
    ```

    The script will automatically convert all `.vtt` files in the specified directory to `.srt` format and save them in the same directory.

## Example

If you have a directory `/home/user/subtitles/` containing `.vtt` files, you would set the `directory` variable in the `main()` function like this:

```python
directory = r"/home/user/subtitles/"