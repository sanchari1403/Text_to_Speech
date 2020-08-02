from text_to_speech_converter import text_to_speech
import PyPDF2 

def read_from_txt(filepath):
    with open(filepath, 'r') as file:
        txt = file.read()
    # txt=file1.read()
    print txt
    text_to_speech(txt)
    file.close()

def read_from_pdf(filepath):
    # creating a pdf file object 
    pdfFileObj = open(filepath, 'rb') 
        
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        
    # getting number of pages in pdf file 
    pages=pdfReader.numPages

    text=''
    # creating a page object
    for i in range(0,pages): 
        pageObj = pdfReader.getPage(i)     
        # extracting text from page 
        text=pageObj.extractText()
        text_to_speech("Reading from page number"+str(i+1)+"of"+str(pages)) 
        text_to_speech(text) 
        
    # print(text)   
    # text_to_speech(text) 
    # closing the pdf file object 
    pdfFileObj.close() 


if __name__ == "__main__":

    choice=input("Type of file: Press 1 for .txt file and press 2 for .pdf file: ")
    filepath=raw_input("Enter the full filepath: ")
    if choice == 1:
        read_from_txt(filepath)
    elif choice == 2:
        read_from_pdf(filepath)
    else:
        print("Please upload a file in the supported formats!")