"""
Configuration settings for the AV Crash Scraper
"""

# API Configuration
API_BASE_URL = 'https://www.avcrashes.net/api/accidents/'

# Headers for API requests
API_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0',
    'Accept-Language': 'en-US,en;q=0.8',
    'ApiJwtToken': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzNDM0MzQyMzI0IiwibmFtZSI6Ik1hcnRpbiBCdXJlcyIsImlhdCI6MjQyNDQzMzI0M30.MPq6DUA7EhVdaEi_mmGtDMPnem9l4bzvn4ZOOP39R-Q'
}

# Scraping Configuration
DEFAULT_OUTPUT_DIR = "data"
DEFAULT_DELAY = 0.5  # Seconds between requests
DEFAULT_RETRY_DELAY = 1.0  # Seconds between retry requests
DEFAULT_MAX_ACCIDENTS = 1000

# Logging Configuration
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'INFO'
LOG_FILE = 'scraper.log' 