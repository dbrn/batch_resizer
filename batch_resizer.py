# python 3.5+
import cv2
import glob
import argparse


def main():
    default_resize = (100, 100)
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=str, nargs=1, help="Path where the "
                                                             "files to resize "
                                                             "are")
    parser.add_argument("-s", "--size", type=str, nargs=1, help="Size of the "
                                                                "resized image"
                                                                "(eg. 100x100)")
    args = parser.parse_args()
    if args.size:
        default_resize = tuple(map(int, args.size[0].split("x")))
    files = glob.glob(f"{args.directory[0]}/*.*")
    for file in files:
        print(file)
        img = cv2.imread(file, 1)
        resized_img = cv2.resize(img, default_resize)
        extension = file.rindex(".")
        cv2.imwrite(f"{file[0:extension]}_res_{file[extension:]}", resized_img)


if __name__ == "__main__":
    main()
