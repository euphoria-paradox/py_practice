# Pictures on the go.
# This is a program to determine the number of images that can be stored
# a given USB (flash) drive whose storage is in GB.
# 
# The number of images is calculated for GIF,JPEG,PNG & TIFF image file formats.
# Assumption is that all images are of resolution 800x600 pixels
#
#  Compression ratios are given as:
# GIF - 256 colors -8 bits-5:1 compression
# JPEG- 16 million colors - 24 bits - 25:1
# PNG - '' '' - 24 bits - 8:1
# TIFF - 280 million colors - 48 bits - n/a

# Program greeting
print('''Welcome to the program
This is a program to determine the number of images that can be stored a given USB 
(flash) drive whose storage is in GB based on different image formats.''')

# input of USB size
usb_size = int(input('Enter the size of USB in GB: '))
usb_size_bytes = usb_size*1e9

# determine the size of each file in bytes of different image formats. color depth = 8 bits = 1 byte
gif_size = (800*600*1)/5
jpeg_size = (800*600*3)/25
png_size =(800*600*3)/8
tiff_size = (800*600*6)

# Determine the number of images of each type that can be stored
num_images_gif = usb_size_bytes//gif_size
num_images_jpeg = usb_size_bytes//jpeg_size
num_images_png =usb_size_bytes//png_size
num_images_tiff = usb_size_bytes//tiff_size

# Display the result

print('\n',format(num_images_gif,','),'images in GIF format can be stored in',usb_size,'GB of storage\n',
    format(num_images_jpeg,','),'images of JPEG format can be stored in',usb_size,'GB of storage\n',
    format(num_images_png,','),'images in PNG format can be stored in',usb_size,'GB of storage\n',
    format(num_images_tiff,','),'images in TIFF format can be stored',usb_size,'GB of storage\n')