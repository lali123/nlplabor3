import asyncio
import httpx

async def fetch_status(client, url):
    response = await client.get(url)
    return response.status_code

async def check_all_services(urls):
    async with httpx.AsyncClient() as client:
        tasks = [fetch_status(client, url) for url in urls]
        return await asyncio.gather(*tasks)
