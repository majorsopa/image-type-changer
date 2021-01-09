# Import the stuff
import tkinter as tk, os
from PIL import Image, ImageTk


# Set image path to the current directory wherever you are
imageDirname = os.path.dirname(__file__)
imagePath = os.path.join(imageDirname, 'images to change/')
# Set asset path to the current directory wherever you are
assetDirname = os.path.dirname(__file__)
assetPath = os.path.join(imageDirname, 'assets/')


def change(endFormat, preserveAlpha):
    

    f = []

    for (dirpath, dirnames, filenames) in os.walk(imagePath):
    
        f.extend(filenames)
  
        j = 0

        for x in filenames:

            # Get rid of the last . and whatever is past it
            file = filenames[j]
            splitat = file.rfind('.') + 1

            r = file[splitat:]
            file = file[:-len(r)]

            # Opem that image
            im = Image.open(imagePath + filenames[j])

            if preserveAlpha == True:   
                im.convert('RGBA').save(imagePath + file + endFormat.lower(), endFormat)

            if preserveAlpha == False:
                im.convert('RGB').save(imagePath + file + endFormat.lower(), endFormat)

            j += 1

        break


# Make the window and set window name
root = tk.Tk(className = 'image changer')
# Set background color
root.configure(bg ='#232323')
# Set window size
root.geometry('200x100')
# Make unable to be resized
root.resizable(False, False)
# Set icon
root.iconphoto(False, tk.PhotoImage(file = assetPath + 'icon.png'))

# Set the list of file types to transfer between
optionsList = [
    'PNG',
    'JPEG',
    'ICO',
    'WEBP',
    'TIFF',
    'BMP'
]

# Make StringVar() for the label of the dropdown
optionVariable = tk.StringVar()
optionVariable.set(optionsList[0])


# Make labels
lblTo = tk.Label(text = 'to', bg = '#232323', fg = '#E16D00')


# Make dropdown for all the different options
opt = tk.OptionMenu(root, optionVariable, *optionsList)
opt.config(bg = '#E16D00', fg = 'BLACK')
opt['highlightthickness']=0
opt['menu'].config(bg='#E16D00', fg = 'BLACK')


# Make buttons
#if optionVariable.get() == 'PNG' or optionVariable.get() == 'ICO' or optionVariable.get() == 'WEBP' or optionVariable.get() == 'TIFF' or optionVariable.get() == 'BMP':
btnConvert = tk.Button(text = 'Convert (preserve alpha)', bg = '#E16D00', fg = 'BLACK', command = lambda: change(optionVariable.get(), True))
btnConvertNoAlpha = tk.Button(text = "Convert (don't preserve alpha)", bg = '#E16D00', fg = 'BLACK', command = lambda: change(optionVariable.get(), False))


# Stick all the stuff in the window
lblTo.grid(row = 0, column = 0)
opt.grid(row = 0, column = 1)
btnConvert.grid(row = 1, column = 1)
btnConvertNoAlpha.grid(row = 2, column = 1)

# Run mainloop to actually have the window
root.mainloop()
