import zlib
from typing import Sequence, MutableMapping, Callable, Iterable

from frozendict import frozendict


def createList(bytestrings: Iterable[bytes],
							 extract_name_func: Callable = lambda x: x) -> Sequence[MutableMapping[str, str]]:
	return [{"name": extract_name_func(bs), **iterHash(bs)} for bs in bytestrings]


def iterHash(bs: bytes, struct=frozendict({"crc32": zlib.crc32})) -> MutableMapping[str, str]:
	return {k: str(f(bs)) for (k, f) in struct.items()}
