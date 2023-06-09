from pathlib import Path

SCHEME = "http"
HOST = "demostore.supersqa.com"
URL = f"{SCHEME}://{HOST}"
USER_LOGIN = f'login' #wstaw w razie potrzeby
USER_PASSWORD = f'password' #wstaw w razie potrzeby

# Run tests in headless mode
HEADLESS = False
WINDOW_SIZE = "1920,1080"

#View tests reports
BASE_DIR = Path(__file__).resolve().parent.parent

