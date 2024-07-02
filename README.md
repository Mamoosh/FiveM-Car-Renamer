# FiveM Car Renamer

## Title: Batch Rename Car Models and Meta Files

## Description

This Python script is designed to help you rename car models and their corresponding meta files in the FiveM game modification platform. It allows you to replace a specific substring in both the file names and the content of the meta files.

The script can be useful when you need to update car names, fix typos, or make other changes to the car models in your FiveM server.

## Features

- Renames files with a specific substring in their names
- Modifies the content of meta files to replace a specific substring
- Supports various file encodings (UTF-8, UTF-16, ISO-8859-1, Windows-1252)
- Handles XML parsing errors gracefully
- Provides feedback on the changes made during the process

## Usage

1. Ensure you have Python installed on your system.
2. Save the script to a file (e.g., `car_renamer.py`).
3. Open the script and update the following variables to match your specific use case:
   - `path`: the directory containing the car models and meta files
   - `old_substring`: the substring you want to replace
   - `new_substring`: the new substring to replace the old one
4. Run the script using the following command:

   ```
   python car_renamer.py
   ```

5. The script will start processing the files in the specified directory. It will rename the files and update the content of the meta files accordingly.
6. The script will provide feedback on the changes made during the process.

## Disclaimer

This script is provided as-is, without any warranty or guarantee. It is your responsibility to ensure that you have the necessary permissions and backups before running the script. The script is intended for use by experienced FiveM server administrators who understand the potential impact of modifying game files.
