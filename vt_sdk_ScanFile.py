"""
檔案安全性掃描測試
"""

from dotenv import load_dotenv
import os, asyncio
import vt

load_dotenv()
API_KEY = os.getenv('VIRUSTOTAL_API_KEY')

async def scan_file(client, file_path):
    # 1. 開啟檔案 (二進位模式)
    with open(file_path, "rb") as f:
        # 2. 上傳並掃描 (使用非同步方法)
        analysis_object = await client.scan_file_async(file=f)
    # 3. 等待分析結果
    completed_analysis = await client.wait_for_analysis_completion(analysis_object)
    # 4. 回傳統計數據
    return completed_analysis.stats

async def main():
    async with vt.Client(API_KEY) as client:
        with open("geek.exe", "rb") as f: #我用geek.exe做測試
            stats = await scan_file(client, "geek.exe")
            print(stats)

if __name__ == '__main__':
    asyncio.run(main())