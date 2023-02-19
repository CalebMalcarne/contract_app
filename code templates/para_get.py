from docx import Document
from docx.shared import Pt

def get_paragraph(num):
    document = Document("docs/Contract.docx")
    paragraph = document.paragraphs[num].text
    return paragraph

def man_select():    
    while(True):
        user_num = int(input("> "))
        print(get_paragraph(user_num))
        print('\n')
        
man_select()
        