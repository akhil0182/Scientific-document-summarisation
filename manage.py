import pdf2txt
import extractor1
import pdf_downloader
import os 
os.system('python pdf2txt.py base.pdf')
extractor1.extrac()
pdf_downloader.download()

