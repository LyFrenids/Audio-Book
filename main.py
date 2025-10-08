import pyttsx3
import PyPDF2
from tkinter.filedialog import*

book = askopenfilename()
reader = PyPDF2.PdfReader(book)
pages = len(reader.pages)

for i in range (pages):
    page = reader.pages[i]
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()