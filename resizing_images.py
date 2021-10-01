#importing necessary libraries
import os
from PIL import Image

#path to the location of all images folder
path= r'C://Users//user//Documents//python38//deeplearning//oralclassification//newdata//Normal'
#new path to save the resized images
newpath= r'C://Users//user//Documents//python38//deeplearning//oralclassification//newdata//NL'


if __name__ == "__main__":
    
    #looping over all images from the directory
    for f in os.listdir(path):
        
        if os.path.isfile(os.path.join(path,f)):

            f_text, f_ext= os.path.splitext(f)

            f_ext= f_ext[1:].upper()

            if f_ext in extensions:

#                 print(f)

                image = Image.open(os.path.join(path,f))

                width, height= image.size
             
                #resizing all images to required sizes

                image = image.resize((512,512), Image.ANTIALIAS)

                image.save(os.path.join(newpath,f))