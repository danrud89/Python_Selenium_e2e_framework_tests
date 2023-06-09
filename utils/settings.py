from pathlib import Path

SCHEME = "http"
HOST = "demostore.supersqa.com"
URL = f"{SCHEME}://{HOST}"
USER_LOGIN = f'login'
USER_PASSWORD = f'password'

#Tests timeouts (seconds)
SYSTEM_DELAY = 1
RENDER_PAGE_DELAY = 2
SERVER_DELAY = 5
LOAD_DATA_DELAY = 10
GET_DATA_FROM_SERVER_DELAY = 15

# Run tests in headless mode
HEADLESS = False
WINDOW_SIZE = "1920,1080"

#View tests reports
BASE_REPORTS_DIR = Path(__file__).resolve().parent.parent
ALLURE_REPORTS_PATH = f'--alluredir={BASE_REPORTS_DIR}/reports'
ALLURE_MAKE_REPORT = f'allure serve {BASE_REPORTS_DIR}/reports'

