import PyPDF2
import os

path = "D:\Programming\Mini-Projects-Python\EntryPDFs"
finalPDFName = "MergedPDFFiles.pdf"

pdfWritter = PyPDF2.PdfFileWriter()
pdfOutputFile = open(finalPDFName, "wb")

for file in os.listdir(path):
    with open(F'{path}\{file}', "rb") as pdfFile:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)

        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWritter.addPage(pageObj)

        pdfWritter.write(pdfOutputFile)

pdfOutputFile.close()
