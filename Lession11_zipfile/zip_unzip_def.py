import os
import zipfile
import hashlib

def zip(folder, zip_file):
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        folder_name = os.path.basename(folder)
        zipf.write(folder, folder_name)
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, folder)
                zipf.write(file_path, os.path.join(folder_name, rel_path))
    print(f"Compress Done! Output: {zip_file}")

def unzip(zip_file, target_path):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(target_path)
        print(f"Extract Done! Output: {target_path}")

def check_md5(file, chunk_size = 2048):
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        while chunk := f.read(chunk_size):
            md5.update(chunk)
    return md5.hexdigest()

def check_folder_md5(folder, chunk_size = 2048):
    md5 = hashlib.md5()
    for root, dirs, files in os.walk(folder):
        for file in files:
            with open(file, 'rb') as f:
                while chunk := f.read(chunk_size):
                    md5.update(chunk)
    return md5.hexdigest()

def main():
    home_path = os.path.expanduser('~')
    folder = os.path.join(home_path, 'PythonCode/Lession11_zipfile/log')
    zip_file = os.path.join(home_path, 'Desktop/log.zip')
    target_path = os.path.join(home_path, 'Desktop')

    print(f"Before compressed, the MD5 value of the folder is {check_folder_md5(folder)}")
    zip(folder, zip_file)
    print(f"The MD5 value of the ZIP file is {check_md5(zip_file)}")
    unzip(zip_file, target_path)
    print(f"The MD5 value of the folder is {check_folder_md5(os.path.join(target_path, 'log'))}")
  

if __name__ == '__main__':
    main()