from PIL import Image
import os
# PIL.Image.open(dogPic, mode='r')   DOESN'T work!! :(
image1 = Image.open('dogPic.jpg')
image1.show()
# im = Image.new("RGB",(250,250))
# print(im)

# size_300=(300,300)       FOR RESIZING BUT ?????????
# for f in os.listdir('.'):
#     if f.endswith('.jpg'):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
#
#         i.thumbnail(size(size_300))
#         i.save('pngs/{}.png'.format(fn))
