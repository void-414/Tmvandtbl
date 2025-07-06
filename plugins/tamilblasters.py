import re
import asyncio
import requests
import feedparser
from bot import user
from .database import db
from bs4 import BeautifulSoup
from config import TBL_URL, TBL_LOG, GROUP_ID

async def tamilblasters_rss(user):
    feed = feedparser.parse(TBL_URL+"index.php?/discover/all.xml/")
    count = 0
    data = []
    global real_dict
    real_dict = {}
    for entry in feed.entries:
        if count >= 40:
            break
        count += 1
        data.append(entry.link)
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Connection': 'Keep-alive',
        'sec-ch-ua-platform': '"Windows"',
    }
    for url in data:
        html = requests.request("GET", url , headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        pattern = re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        big_title = soup.find_all('a')
        all_titles = []
        file_link = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])

        for a in soup.find_all('a', {"data-fileext": "torrent", 'href': True}):
            href = a.get('href', '')
            if href:
                file_link.append(href)
                clean_title = a.text.strip()
                all_titles.append(clean_title)

        for p in range(0, len(mag)):
            try:
                if not await db.is_tbl_exist(all_titles[p], file_link[p], mag[p]):
                    # Send Channel
                    await user.send_message(
                        chat_id=TBL_LOG, 
                        text=f"<b>/qbleech {file_link[p]}\n\nFile Name :- {all_titles[p]}</b>", 
                        disable_web_page_preview=True
                    )
                    # Send Group
                    msg = await user.send_message(
                        chat_id=GROUP_ID, 
                        text=f"<b>{file_link[p]}\n\nFile Name : {all_titles[p]}</b>", 
                        disable_web_page_preview=True
                    )
                    await user.send_message(chat_id=GROUP_ID, text="/qbleech", reply_to_message_id=msg.id)
                    print(f"added working...")
                    await db.add_tbl(all_titles[p], file_link[p], mag[p])
                    await asyncio.sleep(3)
            except Exception as e:
                print(e)
                pass
