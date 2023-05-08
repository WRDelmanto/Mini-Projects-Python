from pdfrw import PdfReader, PdfWriter
import os


def mergePdfFile(path, output_pdf):
    # Create a PDF writer object
    pdfWritter = PdfWriter()

    # Open the output PDF file in write mode
    pdfOutputFile = open(output_pdf, "wb")

    # Loop through all files in the specified path
    for file in os.listdir(path):
        # Check if the file is a PDF file
        if file.endswith(".pdf"):
            # Open the PDF file in read mode
            with open(F'{path}\{file}', "rb") as pdfFile:
                # Create a PDF reader object
                pdfReader = PdfReader(pdfFile)

                # Loop through all pages in the PDF file
                for pageNum in range(pdfReader.numPages):
                    # Get the page object for the current page
                    pageObj = pdfReader.getPage(pageNum)

                    # Add the page object to the PDF writer object
                    pdfWritter.addPage(pageObj)

                # Write the PDF writer object to the output PDF file
                pdfWritter.write(pdfOutputFile)

    # Close the output PDF file
    pdfOutputFile.close()


mergePdfFile("temp", "mergedPdfs.pdf")
