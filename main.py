import os

def vtt_to_srt(vtt_file_path, srt_file_path):
    """
    Converts a .vtt (WebVTT) subtitle file to a .srt (SubRip Subtitle) file.

    Args:
        vtt_file_path (str): The file path of the .vtt file to convert.
        srt_file_path (str): The file path where the converted .srt file will be saved.
    """
    with open(vtt_file_path, 'r', encoding='utf-8') as vtt_file:
        lines = vtt_file.readlines()  # Read all lines from the VTT file

    srt_lines = []  # Initialize a list to hold the SRT file lines
    index = 1  # Subtitle index starts at 1

    for line in lines:
        if 'WEBVTT' in line.strip():
            continue  # Skip the line containing "WEBVTT"
        if '-->' in line:
            srt_lines.append(f"{index}\n")  # Add the index number
            index += 1
            # Convert the timestamp format from VTT to SRT (replace '.' with ',')
            timestamp = line.replace('.', ',').strip()
            srt_lines.append(f"{timestamp}\n")
        elif line.strip() != '':
            srt_lines.append(f"{line.strip()}\n")  # Add non-empty lines as subtitle text
        else:
            srt_lines.append('\n')  # Add a blank line after each subtitle block

    # Ensure the last subtitle block ends with a blank line
    if not srt_lines[-1] == '\n':
        srt_lines.append('\n')

    with open(srt_file_path, 'w', encoding='utf-8') as srt_file:
        srt_file.writelines(srt_lines)  # Write the SRT lines to the output file

def convert_all_vtt_in_directory(directory):
    """
    Converts all .vtt files in a directory to .srt files.

    Args:
        directory (str): The directory containing .vtt files to convert.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".vtt"):
            vtt_file_path = os.path.join(directory, filename)
            srt_file_path = os.path.join(directory, filename.replace('.vtt', '.srt'))
            vtt_to_srt(vtt_file_path, srt_file_path)
            print(f"Converted: {filename} to {filename.replace('.vtt', '.srt')}")

def main():
    """
    Main function that defines the directory and calls the conversion function.

    Replace 'path/to/directory' with the actual path containing .vtt files.
    """
    directory = r"path/to/directory"
    convert_all_vtt_in_directory(directory)

# Example usage
if __name__ == "__main__":
    main()
