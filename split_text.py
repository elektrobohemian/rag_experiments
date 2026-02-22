from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_docs(documents, chunk_size=500, chunk_overlap=100):
    # define the splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    # use the splitter to split docs into documents
    doc_parts=[]
    file_parts=[]
    for doc in documents:
        doc_parts.append(doc[0])
        file_parts.append({'file_name':doc[1]}) # we have to create a dict in order to use it as metadata below

    print(f"DEBUG DOC_PARTS is of type: {type(doc_parts)}")
    documents = splitter.create_documents(doc_parts,metadatas=file_parts)

    print(f"DEBUG CHUNKS is of type: {type(documents)}")

    # debug
    #print(f"DEBUG - Generated documents:")
    #for chunk in documents:
    #    print(f"\tChunk: {chunk}")
    return documents