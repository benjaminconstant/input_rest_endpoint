git clone https://github.com/benjaminconstant/input_rest_endpoint.git
cd input_rest_endpoint
mkvirtualenv input_rest_endpoint
pip install -r requirements.txt
uvicorn main:app --reload

----------------------------------

POST localhost:8000/b64/ payload_json = {"file": "base64 string"}