import BeautifulSoup
import requests
import openpyxl

# Initialize Excel workbook and worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.append(["Website URL", "Email"])

# List of URLs to scrape emails from
urls = [
    "https://apps.shopify.com/judgeme"

]

# Function to extract email from text
def extract_email(text):
    import re
    email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
    emails = email_pattern.findall(text)
    if emails:
        return emails[0]
    return None

# Iterate through URLs and extract emails
for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            email = extract_email(soup.get_text())
            if email:
                worksheet.append([url, email])
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")

# Save Excel file
workbook.save("email_data.xlsx")
