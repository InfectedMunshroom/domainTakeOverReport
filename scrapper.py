from playwright.sync_api import sync_playwright
import sys
import requests

def scrape_site(url):
    with sync_playwright() as p:
        browser = p.firefox.launch()
        context = browser.new_context()

        # Capture requests and responses
        def log_request(request):
            print(f"➡️ Request: {request.method} {request.url}")
            headers = request.headers
            sec_fetch_site = headers.get("sec-fetch-site")
            print(f"   sec-fetch-site: {sec_fetch_site}")
            response = requests.head(url)
            if 'sec-fetch-site' in headers:
                print(f"   sec-fetch-site: {headers['sec-fetch-site']}")
                if headers['sec-fetch-site'] == 'cross-site' and request.headers['sec-fetch-site']:
                    print("   🚨 Cross-site request detected!")

        def log_response(response):
            if response.status in [301, 302, 307, 308]:
                print(f"🔁 Redirected: {response.status} from {response.url}")
        
        context.on("request", log_request)
        context.on("response", log_response)

        page = context.new_page()
        try:
            page.goto(url, timeout=15000)
            print(f"✅ Page loaded: {url}")  
        except Exception as e:
            print(f"❌ Error loading page: {e}")

        browser.close()



if __name__ == "__main__":
    file_path = input("Enter the path to the file containing the URL: ").strip()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                input_url = line.strip()
                if not input_url.startswith("http"):
                    input_url = "https://" + input_url

                scrape_site(input_url)

    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")



#               BASE Scrapper

##import requests
##url = "https://chennairivers.gov.in/"
##response = requests.head(url)
##print(response.headers) # prints the entire header as a dictionary
##print(response.headers.get("Content-Length", "Content-Length not found")) # prints a specific section of the 
###dictionary
