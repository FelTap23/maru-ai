from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import BaseDocumentTransformer, Document
from fastapi import FastAPI
from choya.controller.sum_controller import router as sum_router
from choya.controller.completion_controller import router as comp_router

import logging
logger = logging.getLogger("maru_ai_main")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def rag_logic_here():
    pdf = PdfReader("test/resources/ley_agraria.pdf")
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 2000,chunk_overlap =100)
    chunks = text_splitter.split_text(text)
    logger.info(chunks[0])
    logger.info("*"*100)
    logger.info(chunks[1])
    logger.info("*"*100)
    logger.info(chunks[2])

#Creation of the fast api object
app = FastAPI()

app.include_router(sum_router)

app.include_router(comp_router)