
import asyncio
from aiohttp import ClientSession, TCPConnector, ClientTimeout

DEFAULT_TIMEOUT = ClientTimeout(total=30)

class AsyncHTTPClient:
    def __init__(self, max_conn_per_host: int = 10):
        self.connector = TCPConnector(limit_per_host=max_conn_per_host, ssl=False)
        self.session = None

    async def __aenter__(self):
        self.session = ClientSession(connector=self.connector, timeout=DEFAULT_TIMEOUT)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def get_text(self, url: str):
        assert self.session is not None
        start = asyncio.get_event_loop().time()
        async with self.session.get(url, allow_redirects=True) as resp:
            text = await resp.text(errors="ignore")
            elapsed = asyncio.get_event_loop().time() - start
            return text, dict(resp.headers), resp.status, elapsed
