from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from scraper import scrape_internshala
from nlp_engine import RoleMatcher

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

matcher = RoleMatcher()

# Mount frontend directory for static assets if needed (though we're mostly using one file)
# Using absolute path for reliability
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
def read_root():
    return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/search")
def search_jobs(role: str):
    jobs = scrape_internshala(role)

    ranked = matcher.match(role, jobs)
    return ranked[:10]
