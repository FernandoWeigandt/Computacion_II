
import json
import struct

_HDR = struct.Struct("!I")  # uint32 BE

def pack_message(obj: dict) -> bytes:
    payload = json.dumps(obj, ensure_ascii=False).encode("utf-8")
    return _HDR.pack(len(payload)) + payload

def read_exact(sock, n: int) -> bytes:
    buf = bytearray()
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("Socket closed")
        buf.extend(chunk)
    return bytes(buf)

def recv_message(sock) -> dict:
    header = read_exact(sock, _HDR.size)
    (length,) = _HDR.unpack(header)
    payload = read_exact(sock, length)
    return json.loads(payload.decode("utf-8"))
