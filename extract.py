import datetime, time
import requests
import selectorlib


URL = "http://programmer100.pythonanywhere.com/"

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def store(extracted):
    with open("data.txt", "a") as file:
        file.write(str(datetime.datetime.now()) + "," + extracted + "\n")

#def read(extracted):
#    with open("data.txt", "r") as file:
 #       return file.read()

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        store(extracted)
        time.sleep(2)
 #       content = read(extracted)
 #       if extracted != "No upcoming tours":
 #           if extracted not in content:
 #               store(extracted)
#              send_email(message = "Hey, new event was found")
#        time.sleep(2)
