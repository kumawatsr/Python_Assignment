import os
import shutil


def organize_files(dir):
    file_counts = {}
    total_files_moved = 0

    for filename in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, filename)):
            file_extension = os.path.splitext(filename)[1][1:].lower()
            destination_folder = os.path.join(dir, file_extension)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            source_file = os.path.join(dir, filename)
            destination_file = os.path.join(destination_folder, filename)

            try:
                shutil.move(source_file, destination_file)
                total_files_moved += 1
                if file_extension in file_counts:
                    file_counts[file_extension] += 1
                else:
                    file_counts[file_extension] = 1
            except Exception as e:
                print(f"Error moving file '{filename}': {str(e)}")

    print("Files organized successfully")
    print("Total files moved:", total_files_moved)
    print("File counts by extension:")
    for extension, count in file_counts.items():
        print(f"{extension}: {count} occurences")


dir = input("Enter the dir path: ")
organize_files(dir)

"""

Explanation :

1. The code starts by importing the required modules, `os` and `shutil`, which provide functions for file and directory operations.

2. The `organize_files` function is defined, taking the directory path (`dir`) as a parameter.

3. Two variables, `file_counts` and `total_files_moved`, are initialized to keep track of the number of files moved and the count of files by extension.

4. The code iterates over each item in the specified directory using `os.listdir(dir)`.

5. For each item, it checks if it is a file using `os.path.isfile`. If it's not a file (e.g., a directory), it skips to the next iteration.

6. The file extension is extracted using `os.path.splitext(filename)[1][1:].lower()`. It splits the filename into the base name and extension, removes the leading dot from the extension, and converts it to lowercase.

7. The destination folder path is created by joining the original directory path (`dir`) with the file extension using `os.path.join`.

8. If the destination folder does not exist, it is created using `os.makedirs(destination_folder)`.

9. The source file path and destination file path are constructed using `os.path.join`.

10. The code attempts to move the file from the source path to the destination path using `shutil.move`. If successful, it increments the `total_files_moved` counter and updates the `file_counts` dictionary.

11. If an exception occurs during the file move, an error message is printed.

12. After processing all files, the code prints a success message, the total number of files moved, and the count of files by extension using a loop over the `file_counts` dictionary.

13. Finally, the user is prompted to enter the directory path, and the `organize_files` function is called with the provided directory path as the argument.

"""