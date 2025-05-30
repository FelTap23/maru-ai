from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import BaseDocumentTransformer, Document

pdf = PdfReader("test/resources/ley_agraria.pdf")

text = ""
for page in pdf.pages:
    text += page.extract_text()


text_splitter = RecursiveCharacterTextSplitter(chunk_size = 2000,chunk_overlap =100)
chunks = text_splitter.split_text(text)



print(chunks[0])
print("*"*100)
print(chunks[1])
print("*"*100)
print(chunks[2])