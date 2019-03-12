import pdf2txt
import extractor
import pdf_downloader
import os 
os.system('python pdf2txt.py base.pdf')
extractor.extrac()
pdf_downloader.download()

