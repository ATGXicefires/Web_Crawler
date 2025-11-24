___
# Python Web Scraping & VirusTotal API Integration

這是一個 Python 實作練習專案，主要包含兩個領域的功能：
1. **靜態網頁爬蟲**：抓取台灣水庫即時水情資料。
2. **資訊安全 API 整合**：使用 VirusTotal API 進行 URL 安全掃描（包含「通用 HTTP 請求」與「官方非同步 SDK」兩種實作方式）。

## 📂 專案檔案說明

- **`static_web.py`**: 爬取 [台灣水庫即時水情](https://water.taiwanstat.com/) 網站，解析並儲存水庫數據至 `reservoirs.json`。
- **`VirusTotal_API_test.py`**: 使用 `requests` 直接呼叫 VirusTotal API v3 進行 URL 掃描，並將結果存為 `report.json`。
- **`vt_sdk_test.py`**: 使用官方 `vt-py` SDK 與 `asyncio` 實作非同步 URL 掃描。
- **`requirements.txt`**: 專案所需的 Python 套件列表。

## 🚀 環境設定與安裝

請先確認電腦已安裝 Python，接著在專案目錄下執行以下指令，即可一次安裝所有必要的套件：

```bash
pip install -r requirements.txt
```

### 設定 API Key
本專案使用 VirusTotal API，請在專案根目錄建立一個 `.env` 檔案，並填入您的金鑰：

```ini
# .env
VIRUSTOTAL_API_KEY=你的_VirusTotal_API_Key
```

---

## 📖 使用方式

### 1. 執行水庫爬蟲
抓取最新水庫蓄水量資料：
```bash
python static_web.py
```
> 執行後會產生 `reservoirs.json` 檔案。

### 2. 執行 VirusTotal URL 掃描 (通用方法)
使用 Requests 模組進行同步請求：
```bash
python VirusTotal_API_test.py
```
> 執行後會顯示該 URL 是否安全，並產生 `report.json` 報告。

### 3. 執行 VirusTotal URL 掃描 (官方 SDK)
使用官方 SDK 進行非同步請求：
```bash
python vt_sdk_test.py
```
> 執行後會顯示掃描統計結果 (如 malicious, harmless 數量)。
---

- Edit by ATGXicefires