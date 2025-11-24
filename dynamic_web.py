import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # 啟動瀏覽器
        # headless = False 代表有瀏覽器介面
        # slow_mo = 1000 代表每個動作延遲 1 秒 
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        # 建立分頁
        page = await browser.new_page()
        await page.goto("https://www.youtube.com/")
        await page.fill('input[name="search_query"]', 'Python')
        await page.keyboard.press('Enter')
        # await page.click('button[aria-label="Search"]')
        await page.wait_for_timeout(3000)  # 等待 3 秒
        
        # all_inner_texts() 取得多個元素的文字，回傳 list
        # "#"是css id 選擇器，"."是class選擇器
        # title = await page.locator('#video-title').all_inner_texts()
        # print(title)
        
        video_elements = await page.locator('#video-title').all()
        for element in video_elements:
            title = await element.inner_text()
            url = await element.get_attribute('href')
            print(f'Title : {title}\nURL : https://www.youtube.com{url}\n')
            print('-' * 20)
        
        
        # 關閉瀏覽器
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())