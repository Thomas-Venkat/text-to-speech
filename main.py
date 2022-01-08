import PyPDF2
import pyttsx3

path = open("text.pdf", "rb")

pdf_reader = PyPDF2.PdfFileReader(path)

page = pdf_reader.getPage(0)

text = page.extractText()


speak = pyttsx3.init()

speak.say(text)

speak.runAndWait()