import matplotlib.pyplot as plt
from datetime import datetime

# calculate hourly average for visualization
def get_hourly_data(data):
  hourly_data = {}

  for item in data["data"]:
      start_time = item["startTime"]
      value = item["value"]

      time_obj = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S.%fZ")

      hour_key = time_obj.strftime("%Y-%m-%d %H:00")

      if hour_key not in hourly_data:
        hourly_data[hour_key] = {
          "total": 0,
          "count": 0
        }

      hourly_data[hour_key]["total"] += value
      hourly_data[hour_key]["count"] += 1

  # averages
  result = []
  for hour_key in hourly_data:
    total = hourly_data[hour_key]["total"]
    count = hourly_data[hour_key]["count"]
    average = total / count
    result.append((hour_key, average))

  return sorted(result)


def visualize_data(hourly_data, valid_date):
  if not hourly_data:
    print("No data to visualize.")
    return
  
  # use only the hour part for visualization
  hours = [h.split(" ")[1] for h, _ in hourly_data]
  avgs = [s for _, s in hourly_data]

  plt.figure(figsize=(12, 6))
  plt.bar(hours, avgs, color="#457b9d")
  plt.xlabel("Hour")
  plt.ylabel("Average in MW")
  plt.title(f"Hourly wind power production in {valid_date}")
  plt.xticks(rotation=45, ha="right")
  plt.tight_layout()
  plt.show()