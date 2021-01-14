# Import the stuff
import tkinter as tk, os
from PIL import Image, ImageTk


# Set default first image path to the current directory wherever you are
imageDirname = os.path.dirname(__file__)
imagePath = os.path.join(imageDirname, 'images to change/')
# Set default image save path
imageSaveDirname = os.path.dirname(__file__)
toSaveTo = os.path.join(imageSaveDirname, 'final images/')
# Set asset path to the current directory wherever you are
assetDirname = os.path.dirname(__file__)
assetPath = os.path.join(imageDirname, 'assets/')


def change(endFormat, preserveAlpha):
    
    if takeFromEntry.get() != '':
        imagePath = takeFromEntry.get() + '/'
    else:
        imageDirname = os.path.dirname(__file__)
        imagePath = os.path.join(imageDirname, 'images to change/')

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

            if sendToEntry.get() != '' and preserveAlpha == True:
                im.convert('RGBA').save(sendToEntry.get() + '\\' + file + endFormat.lower(), endFormat)

            elif sendToEntry.get() != '' and preserveAlpha == False:
                im.convert('RGB').save(sendToEntry.get() + '\\' + file + endFormat.lower(), endFormat)

            elif sendToEntry.get() == '' and preserveAlpha == True:
                im.convert('RGBA').save(toSaveTo + file + endFormat.lower(), endFormat)

            else:
                im.convert('RGB').save(toSaveTo + file + endFormat.lower(), endFormat)

            j += 1

        break

def instructionsWindow():

    instructionsRoot = tk.Tk(className = 'instructions')
    instructionsRoot.geometry('400x100')
    instructionsRoot.configure(bg ='#232323')
    instructionsRoot.resizable(False, False)
    lblInstructions1 = tk.Label(master = instructionsRoot, text = 'Input the directories, or leave blank for default.')
    lblInstructions1.config(font = ('Arial', 7), fg = '#E16D00', bg = '#232323')
    lblInstructions2 = tk.Label(master = instructionsRoot, text = 'Make sure that the directory that the images are being taken from is ONLY images.')
    lblInstructions2.config(font = ('Arial', 7), fg = '#E16D00', bg = '#232323')
    lblInstructions1.grid(row = 0)
    lblInstructions2.grid(row = 1)


# Make the window and set window name
root = tk.Tk(className = 'image changer')
# Set background color
root.configure(bg ='#232323')
# Set icon
root.iconphoto(True, tk.PhotoImage(file = assetPath + 'icon.png'))
# Set grid weights to center the frames
for x in range(4):
    root.grid_rowconfigure(x, weight=1)
root.grid_columnconfigure(0, weight=1)
# Set window size
root.geometry('250x250')
# Make unresizable
root.resizable(False, False)


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


# Make frames
frmConvertButtons = tk.Frame(bg = '#232323')
frmTitle = tk.Frame(bg = '#232323')
instructionsFrame = tk.Frame(bg = '#232323')


# Make labels
title = tk.Label(master = frmTitle, text = 'Image transformer')
title.config(font = ('Arial', 13), fg = '#E16D00', bg = '#232323')
lblSendTo = tk.Label(master = frmConvertButtons, text = 'Directory to send images to:')
lblSendTo.config(font = ('Arial', 7), fg = '#E16D00', bg = '#232323')
lblTakeFrom = tk.Label(master = frmConvertButtons, text = 'Directory to take images from:')
lblTakeFrom.config(font = ('Arial', 7), fg = '#E16D00', bg = '#232323')


# Make entrys for directories
sendToEntry = tk.Entry(master = frmConvertButtons)
takeFromEntry = tk.Entry(master = frmConvertButtons)


# Make dropdown for all the different options
opt = tk.OptionMenu(
    frmConvertButtons, 
    optionVariable, 
    *optionsList
)
opt.config(bg = '#E16D00', fg = 'BLACK', font = ('Arial', 10))
opt['highlightthickness']=0
opt['menu'].config(bg='#E16D00', fg = 'BLACK', font = ('Arial', 8))


# Make buttons
btnConvert = tk.Button(
    master = frmConvertButtons, 
    text = 'Convert (preserve alpha)', 
    bg = '#E16D00', fg = 'BLACK', 
    command = lambda: change(optionVariable.get(), True)
)
btnConvert.config(font = ('Arial', 9))
btnConvertNoAlpha = tk.Button(
    master = frmConvertButtons, 
    text = "Convert (don't preserve alpha)", 
    bg = '#E16D00', fg = 'BLACK', 
    command = lambda: change(optionVariable.get(), False)
)
btnConvertNoAlpha.config(font = ('Arial', 9))

btnInstructions = tk.Button(
    master = instructionsFrame,
    text = 'Click for instructions',
    bg = '#E16D00', fg = 'BLACK',
    command = instructionsWindow
)
btnConvertNoAlpha.config(font = ('Arial', 9))


# Stick the stuff in the frames
title.grid(row = 0)

opt.grid(row = 1)

btnConvert.grid(row = 2)
btnConvertNoAlpha.grid(row = 3)

lblTakeFrom.grid(row = 4)

takeFromEntry.grid(row = 5)

lblSendTo.grid(row = 6)

sendToEntry.grid(row = 7)

btnInstructions.grid(row = 8)


# Pack frames
frmTitle.grid(row = 0)
frmConvertButtons.grid(row = 1)
instructionsFrame.grid(row = 2, pady = 5)


# Run mainloop to actually have the window
root.mainloop()
