import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def extract_dmv_wait_times(url):
    """
    Extract DMV wait times from the Texas DPS website and save to JSON.
    """
    try:
        # Fetch the webpage
        print(f"Fetching data from {url}...")
        response = requests.get(url)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table with wait times
        table = soup.find('table')

        if not table:
            print("Error: Could not find table in the page")
            return None

        # Extract data
        offices_data = []
        current_office = None

        # Find all table rows
        rows = table.find_all('tr')

        for row in rows:
            # Skip header rows
            if row.find('th', class_='default_class'):
                # This row starts a new office
                office_cell = row.find('th', class_='default_class')
                office_name = office_cell.get_text(strip=True)

                # Get appointment type, availability, and wait time from this row
                cells = row.find_all('td')
                if len(cells) >= 3:
                    appointment_type = cells[0].get_text(strip=True)
                    availability_days = cells[1].get_text(strip=True)
                    wait_time = cells[2].get_text(strip=True)

                    current_office = {
                        'office_name': office_name,
                        'appointment_types': [
                            {
                                'type': appointment_type,
                                'availability_days': availability_days,
                                'average_wait_time': wait_time
                            }
                        ]
                    }
                    offices_data.append(current_office)
            else:
                # This is a continuation row for the same office
                cells = row.find_all('td')
                if len(cells) >= 3 and current_office:
                    appointment_type = cells[0].get_text(strip=True)
                    availability_days = cells[1].get_text(strip=True)
                    wait_time = cells[2].get_text(strip=True)

                    current_office['appointment_types'].append({
                        'type': appointment_type,
                        'availability_days': availability_days,
                        'average_wait_time': wait_time
                    })

        # Create the final data structure
        result = {
            'title': 'Driver License Appointment and Office Wait Times',
            'extraction_date': datetime.now().isoformat(),
            'source_url': url,
            'offices': offices_data
        }

        return result

    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except Exception as e:
        print(f"Error processing data: {e}")
        return None

def save_to_json(data, filename='dmv_wait_times.json'):
    """
    Save extracted data to a JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Data successfully saved to {filename}")
        print(f"Total offices extracted: {len(data['offices'])}")
    except Exception as e:
        print(f"Error saving to JSON: {e}")

def main():
    url = 'https://www.dps.texas.gov/apps/Viewer/Document/Vue/WAITTIMES'

    # Extract data
    data = extract_dmv_wait_times(url)

    if data:
        # Save to JSON
        save_to_json(data)

        # Print sample data
        print("\nSample data (first office):")
        if data['offices']:
            print(json.dumps(data['offices'][0], indent=2))
    else:
        print("Failed to extract data")

if __name__ == '__main__':
    main()
