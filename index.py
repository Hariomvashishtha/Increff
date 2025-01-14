from fastapi import FastAPI
app = FastAPI()
from routes.index import user

app.include_router(user)

# adding the comment to test the git
