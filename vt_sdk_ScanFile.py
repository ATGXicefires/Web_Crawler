"""
檔案安全性掃描測試
"""

from dotenv import load_dotenv
from pathlib import Path
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

def read_file():
    file_list = []
    folder = Path("project")
    for file in folder.iterdir():
        if file.is_file() and file.suffix == ".exe":
            if file.stat().st_size < 650 * 1024 * 1024:
                #print(file.name)
                file_list.append(file)
    return file_list

async def main():
    async with vt.Client(API_KEY) as client:
        file_list = read_file()
        if file_list:
            for file_path in file_list:
                with open(file_path, "rb") as f:
                    stats = await scan_file(client, file_path)
                print(f'{file_path.name}: {stats}')

if __name__ == '__main__':
    asyncio.run(main())