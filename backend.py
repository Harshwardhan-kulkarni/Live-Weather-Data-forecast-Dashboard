import requests

API_key = "55f1fa88786e970829b4dc63731065c7"


def get_date(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_date(place="Tokyo", forecast_days=3, kind="temperature"))
    print(get_date(place="Tokyo", forecast_days=3, kind="Sky"))
