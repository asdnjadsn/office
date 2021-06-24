import pdfplumber
import os
import pandas as pd
import tabula
import numpy

base_path = 'C:\\Users\Administrator\Desktop\论文'
search = 'Appendix'
all_files = [os.path.join(base_path, f) for f in os.listdir(base_path) if 'pdf' in f]
for file in all_files:
    try:
        with pdfplumber.open(file) as pdf:
            for i in range(len(pdf.pages)):
                page_text = pdf.pages[i].extract_text()
                if search in page_text:
                    print(file)
    except:
        print('error', file)
