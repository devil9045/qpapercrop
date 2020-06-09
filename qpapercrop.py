import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import glob

name_pdf = glob.glob("*.pdf")
num_pdf = len(name_pdf)
for num in range(num_pdf):

    name = name_pdf[num]
    reader = PdfFileReader(f'{name}', 'r')
    writer = PdfFileWriter()

    for i in range(1, reader.getNumPages()-1):
        page = reader.getPage(i)
        page.cropBox.setLowerLeft((0, 295))
        page.cropBox.setLowerRight((595.275, 295))
        page.cropBox.setUpperLeft((0, 808))
        page.cropBox.setUpperRight((595.275, 808))
        writer.addPage(page)

    outstream = open(f'{name}_cropped.pdf', 'wb')
    writer.write(outstream)
    outstream.close()




