from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = BASE_DIR / "uploads"
CHROMA_DB_DIR = BASE_DIR / "chroma_db"
LOG_DIR = BASE_DIR / "logs"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

LLM_MODEL = "gemini-2.5-flash"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

MAX_RETRIES = 3

REQUEST_TIMEOUT = 60

ENABLE_CACHE = True

print("\n========== CONFIG ==========")
print("Model:", LLM_MODEL)

if GOOGLE_API_KEY:
    print("API Key:", GOOGLE_API_KEY[:10] + "...")
else:
    print("API Key: NOT FOUND")

print("============================\n")