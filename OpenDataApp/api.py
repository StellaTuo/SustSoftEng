import urllib.request, json
import urllib.error

# convert the validated date string into startTime and endTime for the API request
def convert_date(date):
  year, month, day = date.split('/')
  startTime = f"{year}-{month}-{day}T00:00:00Z"
  endTime = f"{year}-{month}-{day}T23:59:59Z"
  return startTime, endTime


def get_data(startTime, endTime):
  url = f"https://data.fingrid.fi/api/datasets/181/data?startTime={startTime}&endTime={endTime}&pageSize=479"

  apiKey = "YOUR_API_KEY_HERE"  # Replace with actual API key

  headers ={
  # Request headers
  'Cache-Control': 'no-cache',
  'x-api-key': apiKey,
  }

  if apiKey == "YOUR_API_KEY_HERE":
    print("API key is not set. Replace the placeholder with actual API key.")
    return None

  try:
    req = urllib.request.Request(url, headers=headers)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req, timeout=10)
    return json.loads(response.read())
  
  except urllib.error.HTTPError as e:
    print(f"HTTP error: {e.code} - {e.reason}")
    return None

  except urllib.error.URLError as e:
    print(f"Network error: {e.reason}")
    return None

  except Exception as e:
    print("Unexpected error.")
    print(e)
    return None