"""from PIL import Image
import stepic
im=Image.open('in.png')
im1=stepic.encode(im,b'Hello Python')
im1.save('in.png','PNG')
im1=Image.open('in.png')
#im1.show()
im2=Image.open('in.png')
stegoImage=stepic.decode(im2)
stegoImage
'Hello Python'
im2.show()"""
import aes as b
from stegano import lsb

secret=lsb.hide("C:/Users/jithu/PycharmProjects/j/im/image17.png","Hello World")
secret.save("./im/frame740.png")
clear_message=lsb.reveal("C:/Users/jithu/PycharmProjects/j/im/frame740.png")
print(clear_message)

