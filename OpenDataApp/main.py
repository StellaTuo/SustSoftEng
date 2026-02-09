from date_validation import validate_date
from api import convert_date, get_data
from plot import get_hourly_data, visualize_data

def main():

  unvalid_date = True
  while unvalid_date:
    date = input("Enter a date between 2014/01/01 and the current date in the format YYYY/MM/DD: ")

    valid_date = validate_date(date)
    if not valid_date:
      print("Invalid date. Please enter a date in the format YYYY/MM/DD and between 2014/01/01 and the current date. \n")
      continue
    else:
      unvalid_date = False

  startTime, endTime = convert_date(valid_date)
  data = get_data(startTime, endTime)

  if data is None:
    print("Failed to retrieve data.")
    return

  hourly_data = get_hourly_data(data)
  visualize_data(hourly_data, valid_date)


if __name__ == "__main__":  
  main()