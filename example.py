#!/usr/bin/env python3
"""
Example usage of the AV Crash Scraper
"""

from main import AVCrashScraper
import logging

# Set up logging to see what's happening
logging.basicConfig(level=logging.INFO)

def example_basic_usage():
    """Basic usage example"""
    print("=== Basic Usage Example ===")
    
    # Create scraper instance
    scraper = AVCrashScraper(output_dir="example_data")
    
    # Scrape just a few accidents for demonstration
    scraper.scrape_range(start=800, end=810, delay=0.5)

def example_custom_range():
    """Custom range example"""
    print("\n=== Custom Range Example ===")
    
    scraper = AVCrashScraper(output_dir="custom_data")
    
    # Scrape a specific range with custom delay
    scraper.scrape_range(start=500, end=520, delay=1.0)

def example_fill_missing():
    """Fill missing files example"""
    print("\n=== Fill Missing Files Example ===")
    
    scraper = AVCrashScraper(output_dir="data")
    
    # Only download missing files
    scraper.scrape_range(start=0, end=100, delay=0.5, skip_existing=True)

def example_get_single_accident():
    """Get single accident example"""
    print("\n=== Single Accident Example ===")
    
    scraper = AVCrashScraper()
    
    # Get data for a specific accident
    accident_data = scraper.get_accident_data(813)
    
    if accident_data:
        print(f"Accident ID: {accident_data['id']}")
        print(f"Date: {accident_data['date']} {accident_data['time']}")
        print(f"Company: {accident_data['company']}")
        print(f"Location: {accident_data['state']}, {accident_data['country']}")
        print(f"Injury: {accident_data['injury']}")
    else:
        print("Failed to get accident data")

if __name__ == "__main__":
    # Run examples
    example_basic_usage()
    example_custom_range()
    example_fill_missing()
    example_get_single_accident()
    
    print("\n=== Examples completed ===")
    print("Check the generated directories for the downloaded data!") 