# Autonomous Vehicle Crash Data Scraper

A Python application that automatically scrapes autonomous vehicle crash data from avcrashes.net using their API.

## Features

- ✅ Automatic data scraping (using API)
- ✅ JSON format data storage
- ✅ Error handling and logging
- ✅ Rate limiting (to avoid overloading the API)
- ✅ Skip existing files functionality
- ✅ Resume from interruption capability

## Installation

1. Clone this repository:
```bash
git clone https://github.com/[username]/av_crash.git
cd av_crash
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
python main.py
```

### Programmatic Usage
```python
from main import AVCrashScraper

# Initialize the scraper
scraper = AVCrashScraper(output_dir="data")

# Scrape data for a specific range
scraper.scrape_range(start=0, end=100, delay=0.5)
```

## Data Structure

Each crash record contains the following information:

- **id**: Crash ID
- **date**: Date of incident
- **time**: Time of incident
- **latitude/longitude**: Location coordinates
- **country/state**: Country and state
- **company**: Company (e.g., Waymo, Tesla)
- **vehicle_model**: Vehicle model
- **mode**: Driving mode (Autonomous/Manual)
- **injury**: Injury status
- **vehicle_damage**: Vehicle damage description
- **incident_description**: Crash description
- **fault**: Fault determination
- **weather**: Weather conditions
- **road_conditions**: Road conditions

## Project Structure

```
av_crash/
├── main.py              # Main application
├── config.py            # Configuration settings
├── example.py           # Usage examples
├── requirements.txt     # Required packages
├── README.md           # This file
├── LICENSE             # MIT License
├── .gitignore          # Git ignore rules
├── data/               # Scraped data (new)
│   └── accident_*.json
└── out_data/           # Existing data
    └── accident_*.json
```

## API Details

This application uses the `https://www.avcrashes.net/api/accidents/` API. The API compiles autonomous vehicle crash reports from DMV (Department of Motor Vehicles) sources.

## Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License.

## Warnings

- Follow API rate limiting rules
- Use data responsibly
- Check API key validity period
- Ensure sufficient disk space for large datasets

## Troubleshooting

### Common Errors

1. **403 Forbidden**: API key may be invalid
2. **429 Too Many Requests**: Rate limiting active, increase delay time
3. **Connection Timeout**: Check internet connection

### Logs

All operations are logged to `scraper.log` file. Check this file when experiencing issues.

## Examples

Run the example script to see different usage scenarios:

```bash
python example.py
```

This will demonstrate:
- Basic usage
- Custom range scraping
- Filling missing files
- Single accident data retrieval 