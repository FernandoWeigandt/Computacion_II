
#!/usr/bin/env python3
import sys, asyncio, aiohttp, json

async def main():
    if len(sys.argv) < 2:
        print("usage: client.py URL [host] [port]")
        return
    url = sys.argv[1]
    host = sys.argv[2] if len(sys.argv) >= 3 else "[::1]"
    port = int(sys.argv[3]) if len(sys.argv) >= 4 else 8000
    endpoint = f"http://{host}:{port}/scrape"
    async with aiohttp.ClientSession() as s:
        async with s.get(endpoint, params={"url": url}) as r:
            print("HTTP", r.status)
            data = await r.json()
            print(json.dumps(data, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
