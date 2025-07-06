import datetime
import motor.motor_asyncio
from config import DATABASE_NAME, DATABASE_URL

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.tmvx = self.db.TamilMV_List
        self.tblx = self.db.TamilBlaster_List

    # TMV 
    def tmv(self, Name, link, url):
        return dict(
            FileName = Name,
            magnet_link = link,
            magnet_url = url,
            upload_date=datetime.date.today().isoformat()
        )

    async def add_tmv(self, Name, link, url):
        user = self.tmv(Name, link, url)
        await self.tmvx.insert_one(user)

    async def is_tmv_exist(self, Name, link, url):
        user = await self.tmvx.find_one({'magnet_url': url})
        return True if user else False

    # TBL 
    def tbl(self, Name, link, url):
        return dict(
            FileName = Name,
            magnet_link = link,
            magnet_url = url,
            upload_date=datetime.date.today().isoformat()
        )

    async def add_tbl(self, Name, link, url):
        user = self.tbl(Name, link, url)
        await self.tblx.insert_one(user)

    async def is_tbl_exist(self, Name, link, url):
        user = await self.tblx.find_one({'magnet_url': url})
        return True if user else False
        
db = Database(DATABASE_URL, DATABASE_NAME)
