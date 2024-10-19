from fastapi import FastAPI
import base64
import pickle

app = FastAPI()
glbl_state = None

@app.get("/api/load")
def load_data(data: str):
  global glbl_state
  binary = base64.b64decode(data)
  glbl_state = pickle.loads(binary)
  return {"success" : True}

@app.get("/sqli/")
def show_user(username: str):
    with connection.cursor() as cursor:
      cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)

