# AudioBook

The project is created to convert any pdf or txt book into an audio file. I used tkinter to open up a GUI file dialog selection interface to pick up the text or pdf file. Based on the file extension the file is opened, all its text is transfered to a text file and the file is then closed.Default language of te audio file has been set as English. 
GTTS is then used to convert this sample text into audio file and the os is used to play this file.

Pre-requisites:
Import packages tkinter, PyPDf2, gtts
