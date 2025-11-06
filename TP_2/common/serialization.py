
import base64

def b64encode(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")

def b64decode(s: str) -> bytes:
    return base64.b64decode(s.encode("ascii"))
