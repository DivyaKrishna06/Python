from PIL import Image

im = Image.open("lego_movie.jpg")
w, h = im.size

## Crop out three columns from the image
## Note: the crop function returns a new image
part1 = im.crop((0, 0, int(w/3), h))
part2 = im.crop((int(w/3), 0, int(2*w/3), h))
part3 = im.crop((int(2*w/3), 0, w, h))

## Create a new image
newim = Image.new("RGB", (w, h))

## Paste the images in different order
## Note: the paste function changes the image it is applied to
newim.paste(part3, (0, 0))
newim.paste(part1, (int(w/3), 0))
newim.paste(part2, (int(2*w/3), 0))
newim.show()
