import base64
import magic
import crud
from fastapi import HTTPException
from mimetypes import guess_extension
from uuid import uuid4
from pdf2image import convert_from_bytes
from database import data_folder

def get_item_src(cid, i=0):
    return data_folder + cid + '_page_' + str(i+1) + '.png'

def process_pdf(item, db):
    img_list = convert_from_bytes(item.decoded, fmt='png')
    for i, img in enumerate(img_list):
        item.src = get_item_src(item.correlationId, i)
        crud.create_item(item, db)
        img.save(item.src)

def process_png(item, db):
        item.src = get_item_src(item.correlationId)
        crud.create_item(item, db)
        with open(item.src, 'wb') as f:
            f.write(item.decoded)

def process_item(item, db):
    try:
        item.decoded = base64.b64decode(item.file)
    except:
        raise HTTPException(status_code=422, detail="file parsing failed")

    item.correlationId = str(uuid4())
    mime_type = magic.from_buffer(item.decoded, mime=True)
    ext = guess_extension(mime_type)

    if ext == '.pdf':
        process_pdf(item, db)
    elif ext == '.png':
        process_png(item, db)
    else:
        raise HTTPException(status_code=422, detail="File is not PDF or PNG")

    # POST a servizio successivo con questo payload = {'correlationId': item.correlationId}
    return {'correlationId': item.correlationId}