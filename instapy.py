import argparse as argp
import cv2
from instapy.filters import filters as f
from instapy.tests import runtime as r

parser = argp.ArgumentParser(description='A user friendly userface for instapy.', add_help=False)

parser.add_argument("-h", "--help", action="help", \
                    help="Helpful message showing flags and usage of instapy.")

parser.add_argument("-f", "--file", dest="file", \
                    help="The filename of file to apply filter to.")

parser.add_argument("-se", "--sepia", action="store_true", \
                    help="Select sepia filter.")

parser.add_argument("-g", "--gray", action="store_true", \
                    help="Select gray filter.")

parser.add_argument("-sc", "--scale", dest="scale", type=float, \
                    help="Scale factor to resize image.")

parser.add_argument("-i", "--implement", choices=["python", "numpy", "numba"], \
                    help="Choose the implementation.")

parser.add_argument("-o", "--out", dest="out", \
                    help="The output filename.")

parser.add_argument("-r", "--runtime", action="store_true", \
                    help="Track the runtime of the selected implementation.")

args = parser.parse_args()


if args.file != None:
    filename = "./instapy/photos/originals/" + args.file
    if args.scale != None:
        image = cv2.imread(filename)
        scaled_image = cv2.resize(image, (0, 0), fx=args.scale , fy=args.scale)
        filename = "./instapy/photos/scaled/" + str(args.scale) + "_scaled_"+ args.file
        cv2.imwrite(filename, scaled_image)
    if args.gray:
        if args.out != None:
            outfile = "./instapy/photos/grayscale/" + args.out
        else:
            outfile = None
        if args.implement == "python":
            f.grayscale_image("py", filename, outfile)
        elif args.implement == "numpy":
            f.grayscale_image("np", filename, outfile)
        elif args.implement == "numba":
            f.grayscale_image("nu", filename, outfile)
        else:
            print("No implementation selected.")
    elif args.sepia:
        if args.out != None:
            outfile = "./instapy/photos/sepia/" + args.out
        else:
            outfile = None
        if args.implement == "python":
            f.sepia_image("py", filename, outfile)
        elif args.implement == "numpy":
            f.sepia_image("np", filename, outfile)
        elif args.implement == "numba":
            f.sepia_image("nu", filename, outfile)
        else:
            print("No implementation selected.")
    else:
        print("No filter selected.")
    if args.runtime:
        image = cv2.imread(filename)
        if args.implement != None:
            if args.gray:
                r.runtime("gray", args.implement, image)
            elif args.sepia:
                r.runtime("sepia", args.implement, image)
else:
    print("No input file provided.")
