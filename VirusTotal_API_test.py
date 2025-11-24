"""
用通用方法進行操作(scan url)
"""

from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
API_KEY = os.getenv('VIRUSTOTAL_API_KEY')

url = 'https://www.virustotal.com/api/v3/urls'
headers = {
    'x-apikey': API_KEY
}
payload = {'url': 'www.youtube.com'}

response = requests.post(url, headers=headers, data=payload)

result = response.json()
analysis_id = result['data']['id']

report_url = f'https://www.virustotal.com/api/v3/analyses/{analysis_id}'

request = requests.get(report_url, headers=headers)
report = request.json()

with open("report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False)

malicious = int(report['data']['attributes']['stats']['malicious'])
if malicious > 0:
    print("The URL is malicious.")
else:
    print("The URL is safe.")
