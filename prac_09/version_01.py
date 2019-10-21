import os
import shutil


def main():
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        rename = filename.split('.')[-1]
        try:
            os.mkdir(rename)
        except FileExistsError:
            pass
        print("{}/{}".format(rename, filename))
        os.rename(filename, "{}/{}".format(rename, filename))


main()
