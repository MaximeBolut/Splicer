import os

import image_slicer   # need to install with pip install cmd: python -m pip install image_slicer


goingon = 'y'

while goingon == 'y': 

  path = str(input("Give the complete path of your image (with the image name and its file type(png or jpg...)) \n"))
  print("\n")

  img = os.path.abspath(path)
  
  (directory, name_image) = os.path.split(path)


  slicing = int(input("give the number you want to slice the image in \n"))
  print("\n")

  image_slicer.slice(img, slicing) 

  print(slicing, "slices of the image", name_image ,"have been saved in the same directory (", directory, ")\n")

  goingon = str(input("do you want to continue y/n \n"))


