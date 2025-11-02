from argparse import ArgumentParser

from PIL import Image
import pillow_heif

parser = ArgumentParser()
parser.add_argument("-i", "--image", dest="image", required=True, help="HEIF file name")
args = parser.parse_args()

heif = pillow_heif.read_heif(args.image)
image = Image.frombytes(heif.mode, heif.size, heif.data, "raw")

image_name = args.image.split(".")[0]
image.save(f"./{image_name}.jpg", format="jpeg")
