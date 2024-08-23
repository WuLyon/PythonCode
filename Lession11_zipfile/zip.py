import os
import zipfile

def zip_directory(folder_path, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add the folder itself first
        folder_name = os.path.basename(folder_path)
        zipf.write(folder_path, folder_name)
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Calculate the relative path
                rel_path = os.path.relpath(file_path, folder_path)
                # Add the file to the ZIP file using relative path
                zipf.write(file_path, os.path.join(folder_name, rel_path))

# Specify the path to be zipped and the name of the generated ZIP file.
folder_to_zip = 'path/to/directory'
zip_file_name = 'path/to/file.zip'
zip_directory(folder_to_zip, zip_file_name)
print(f'{folder_to_zip} has been compressed to {zip_file_name}')
