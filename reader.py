import PyPDF2
import textract

filename = "155_ENG_UNI_2018_6_.pdf"

pdfFileObj = open(filename, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 0
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()

text = text.encode('utf-8')
f = open(filename[:-3]+"txt", 'w')
f.write(text)
f.close()

if text != "":
    text = text
