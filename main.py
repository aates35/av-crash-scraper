#!/usr/bin/env python3
"""
Aviation Crash Data Scraper

This script scrapes accident data from avcrashes.net API and saves it as JSON files.
"""

import requests
import json
import time
import os
from pathlib import Path
import logging
from typing import Dict, Any, Optional

from config import (
    API_BASE_URL, API_HEADERS, DEFAULT_OUTPUT_DIR, DEFAULT_DELAY,
    DEFAULT_RETRY_DELAY, DEFAULT_MAX_ACCIDENTS, LOG_FORMAT, LOG_LEVEL, LOG_FILE
)

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AVCrashScraper:
    """Class to handle scraping of aviation crash data."""
    
    def __init__(self, output_dir: str = DEFAULT_OUTPUT_DIR):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Headers for API requests
        self.headers = API_HEADERS
        self.base_url = API_BASE_URL
        
    def get_accident_data(self, accident_id: int) -> Optional[Dict[Any, Any]]:
        """
        Fetch accident data for a specific ID.
        
        Args:
            accident_id: The ID of the accident to fetch
            
        Returns:
            Dictionary containing accident data or None if failed
        """
        try:
            response = requests.get(f'{self.base_url}{accident_id}', headers=self.headers)
            
            if response.status_code == 200:
                data = response.json()['accident']
                if len(data) == 1:
                    return data[0]
                return data
            else:
                logger.warning(f"Failed to fetch accident {accident_id}: Status {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Error fetching accident {accident_id}: {e}")
            return None
    
    def save_accident_data(self, accident_id: int, data: Dict[Any, Any]) -> bool:
        """
        Save accident data to JSON file.
        
        Args:
            accident_id: The ID of the accident
            data: The accident data to save
            
        Returns:
            True if successful, False otherwise
        """
        try:
            filepath = self.output_dir / f"accident_{accident_id}.json"
            
            with open(filepath, "w", encoding='utf-8') as outfile:
                json.dump(data, outfile, indent=4, ensure_ascii=False)
                
            logger.info(f"Saved accident {accident_id} to {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving accident {accident_id}: {e}")
            return False
    
    def file_exists(self, accident_id: int) -> bool:
        """Check if accident file already exists."""
        filepath = self.output_dir / f"accident_{accident_id}.json"
        return filepath.exists()
    
    def scrape_range(self, start: int = 0, end: int = DEFAULT_MAX_ACCIDENTS, delay: float = DEFAULT_DELAY, skip_existing: bool = True):
        """
        Scrape accident data for a range of IDs.
        
        Args:
            start: Starting accident ID
            end: Ending accident ID (exclusive)
            delay: Delay between requests in seconds
            skip_existing: Whether to skip existing files
        """
        logger.info(f"Starting scrape for accidents {start} to {end-1}")
        
        success_count = 0
        error_count = 0
        
        for accident_id in range(start, end):
            try:
                # Skip if file already exists and skip_existing is True
                if skip_existing and self.file_exists(accident_id):
                    logger.debug(f"Skipping accident {accident_id} - file already exists")
                    continue
                
                # Fetch data
                data = self.get_accident_data(accident_id)
                
                if data:
                    if self.save_accident_data(accident_id, data):
                        success_count += 1
                    else:
                        error_count += 1
                else:
                    error_count += 1
                
                # Rate limiting
                time.sleep(delay)
                
            except KeyboardInterrupt:
                logger.info("Scraping interrupted by user")
                break
            except Exception as e:
                logger.error(f"Unexpected error processing accident {accident_id}: {e}")
                error_count += 1
        
        logger.info(f"Scraping completed. Success: {success_count}, Errors: {error_count}")

def main():
    """Main function to run the scraper."""
    scraper = AVCrashScraper()
    
    # Scrape first batch of accidents
    scraper.scrape_range(start=0, end=DEFAULT_MAX_ACCIDENTS, delay=DEFAULT_DELAY)
    
    # Fill in any missing files with longer delay
    logger.info("Filling in missing files...")
    scraper.scrape_range(start=0, end=DEFAULT_MAX_ACCIDENTS, delay=DEFAULT_RETRY_DELAY, skip_existing=True)

if __name__ == "__main__":
    main() 