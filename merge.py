from pypdf import PdfWriter
import argparse

parser = argparse.ArgumentParser(
                    prog='PdfMerger',
                    description='Merges pdf files in the order provided by user.',
                    usage='merge.py file(s)*')

parser.add_argument("files", nargs='*', help="files") # file names are provided as commandline arguments

pdfs = vars(parser.parse_args())['files'] # get pdf names 

merger = PdfWriter() 
for pdf in pdfs: # append each pdf into a single merged pdf
    merger.append(pdf)

# save as "merged.pdf" #TODO: user-defined filename as optional argument
merger.write("merged.pdf")
merger.close()