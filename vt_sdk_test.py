"""
用官方文檔教學進行操作(scan url)
"""

from dotenv import load_dotenv
import os, asyncio
import vt 

file_path = "url/url_list.txt"
load_dotenv()
API_KEY = os.getenv('VIRUSTOTAL_API_KEY')

def read_url():
    with open(file_path, "r") as f:
        url_list = f.read().splitlines()
    return url_list

async def main():
    async with vt.Client(API_KEY) as client:
        for url in read_url():
            report = await client.scan_url_async(url) #scan_url_async為非同步程式 掃描URL
            analysis = await client.wait_for_analysis_completion(report) #中斷程式進程直到取得分析結果
            print(f'{url} : {analysis.stats}')

if __name__ == '__main__':
    asyncio.run(main())