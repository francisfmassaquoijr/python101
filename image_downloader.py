import urllib.request
import random

# Image downloader main function
def Image_Downloader(imageurl):
    random_name = random.randrange(2, 50, 2)
    file_extension = input("Please enter the file extension: ")
    if file_extension == ".png" or file_extension == '.jpg':
        image_name = str(random_name) + file_extension
        downloader = urllib.request.urlretrieve(imageurl, image_name)
    else:
        print("Invalid file extension: ")
        exit(0)

image_url = input("enter the url to download the image: ")

Image_Downloader(image_url)
