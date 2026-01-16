# Texas DMV Wait Times Tracker

Automated daily extraction of Driver License appointment and office wait times from the Texas Department of Public Safety (DPS) website.

## Overview

This project automatically scrapes DMV wait times data from [Texas DPS](https://www.dps.texas.gov/apps/Viewer/Document/Vue/WAITTIMES) and saves it to a JSON file. The data is updated daily via GitHub Actions.

## Data Structure

The extracted data includes:
- **Office names** - All Texas DPS driver license offices
- **Appointment types** - CDL Drive Test, CDL Renewal, Non CDL Drive Test, Original, Renewal/Replacement
- **Availability** - Estimated days until next available appointment
- **Wait times** - Average in-office wait time in hours and minutes

## Files

- `extract_dmv_wait_times.py` - Python script that scrapes and extracts the data
- `dmv_wait_times.json` - Latest wait times data (updated daily)
- `requirements.txt` - Python dependencies
- `.github/workflows/update-dmv-data.yml` - GitHub Actions workflow

## Usage

### Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the extraction script:
   ```bash
   python extract_dmv_wait_times.py
   ```

### Automated Updates

The GitHub Actions workflow runs automatically every day at 8 AM UTC (2 AM CST) to:
1. Fetch the latest data from Texas DPS
2. Extract and format the data
3. Commit and push changes if the data has changed

You can also manually trigger the workflow from the Actions tab in GitHub.

## JSON Output Format

```json
{
  "title": "Driver License Appointment and Office Wait Times",
  "extraction_date": "2026-01-16T...",
  "source_url": "https://www.dps.texas.gov/apps/Viewer/Document/Vue/WAITTIMES",
  "offices": [
    {
      "office_name": "Abilene",
      "appointment_types": [
        {
          "type": "CDL Drive Test",
          "availability_days": "4",
          "average_wait_time": "00:00"
        }
      ]
    }
  ]
}
```

## Data Source

Data is sourced from the official Texas DPS website:
https://www.dps.texas.gov/apps/Viewer/Document/Vue/WAITTIMES

**Note:** The estimates are based on information from the previous business day and do not include earlier appointments that may become available due to cancellations or rescheduling.

## License

This project is for educational and informational purposes. The data belongs to the Texas Department of Public Safety.
