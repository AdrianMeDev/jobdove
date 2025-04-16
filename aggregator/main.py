import logging
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/jobdove.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url = "https://"

running = True


def main():
    response = requests.get(url, headers=header, timeout=10)
    response.raise_for_status()

    # Parse with BeautifulSoup - explicitly using 'html.parser'
    soup = BeautifulSoup(response.content, "html.parser")
    # Keep the script running until signal received


if __name__ == "__main__":
    main()
