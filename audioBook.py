from gtts import gTTS
import os, PyPDF2
from tkinter.filedialog import askopenfilename

filename = askopenfilename()

if filename.endswith('.txt'): #Get file text from txt file
    file1 = open(filename,"r")
    sampleTxt = file1.read()
    file1.close()  
elif filename.endswith('.pdf'): #Get file text from PDF file
    pdfFile = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfPageObj = pdfReader.getPage(0)
    sampleTxt = pdfPageObj.extractText()
    pdfFile.close()

language = 'en'

objtext = gTTS(
    text = sampleTxt,
    lang = language,
    slow = False
)

objtext.save("audioBook.mp3")
os.system("audioBook.mp3") 