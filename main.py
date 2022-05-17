import time
import asyncio
from scripts.nWeather_api import weather_api
import aioschedule as sch
import lunchpage


async def main():
    sch.every().day.at("03:00").do(lunchpage.update)
    await GUI()


async def GUI():
    while True:
        await sch.run_pending()
        lunchpage.root.update()

if __name__ == '__main__':
    asyncio.run(main())


