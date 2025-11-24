"""
用官方文檔教學進行操作(scan url)
"""

from dotenv import load_dotenv
import os, asyncio
import vt 

load_dotenv()
API_KEY = os.getenv('VIRUSTOTAL_API_KEY')

async def main():
    async with vt.Client(API_KEY) as client:
        report = await client.scan_url_async("www.youtube.com") #scan_url_async為非同步程式 掃描URL
        analysis = await client.wait_for_analysis_completion(report) #中斷程式進程直到取得分析結果
        print(analysis.stats)

if __name__ == '__main__':
    asyncio.run(main())