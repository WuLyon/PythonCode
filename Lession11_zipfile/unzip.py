import zipfile

def unzip_file(zip_filename, extract_path):
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        zipf.extractall(extract_path)
        print(f'{zip_filename} has been extracted to {extract_path}')

# Specify the path of the ZIP file to be unzipped and the destination path for extraction.
zip_file_to_unzip = '/path/to/file.zip'
target_extract_path = '/path/to/extract/'
unzip_file(zip_file_to_unzip, target_extract_path)
