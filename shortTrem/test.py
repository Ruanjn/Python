from PIL import Image


# def roll(image, delta):
#     "Roll an image sideways"
#
#     xsize, ysize = image.size
#
#     delta = delta % xsize
#     if delta == 0: return image
#
#     part1 = image.crop((0, 0, delta, ysize))
#     part2 = image.crop((delta, 0, xsize, ysize))
#     part1.load()
#     part2.load()
#     image.paste(part2, (0, 0, xsize - delta, ysize))
#     image.paste(part1, (xsize - delta, 0, xsize, ysize))
#     return image

# im = Image.open("mtl.jpg")
# box = (100, 100, 400, 400)
region = Image.open("part.jpg")
region = region.resize((400, 400))
region = region.rotate(45)
# xsize, ysize = region.size
# delta = 90
# delta = delta % xsize
#
# part1 = region.crop((0, 0, delta, ysize))
# part2 = region.crop((delta, 0, xsize, ysize))
# part1.load()
# part2.load()
# region.paste(part2, (0, 0, xsize - delta, ysize))
# region.paste(part1, (xsize - delta, 0, xsize, ysize))
# region = region.transpose(Image.ROTATE_180)
# im.paste(region, box)


region.show()
# im.show()