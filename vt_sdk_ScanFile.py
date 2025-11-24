"""
檔案安全性掃描測試
"""

from dotenv import load_dotenv
import os, asyncio
import vt

load_dotenv()
API_KEY = os.getenv('VIRUSTOTAL_API_KEY')

async def main():
    async with vt.Client(API_KEY) as client:
        with open("geek.exe", "rb") as f: #我用geek.exe做測試
            file = await client.scan_file_async(file=f)  # 掃描檔案的非同步方法範例
            file_scan = await client.wait_for_analysis_completion(file)  # 等待分析完成
        print(file_scan.stats)

if __name__ == '__main__':
    asyncio.run(main())