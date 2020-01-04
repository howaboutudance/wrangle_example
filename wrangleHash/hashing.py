import zlib, hashlib, pandas as pd, string
from typing import Sequence, MutableMapping
from frozendict import frozendict


def createTable(bytestrings: Sequence[bytes]) -> pd.DataFrame:
	return pd.DataFrame([{**iterHash(bs)} for bs in bytestrings])


def iterHash(bs: bytes, struct = frozendict({"crc32": zlib.crc32})) -> MutableMapping[str, str]:
	return {k: f(bs) for (k, f) in struct.items()}