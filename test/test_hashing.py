import hashlib
from functools import partial
from unittest import TestCase

import pandas as pd

from wrangleHash import hashing, util


class TestGenerateHashList(TestCase):
	def test_iter_hash(self):
		res = dict(hashing.iterHash(b"lorem ipsum", struct={"sha1": lambda bs: hashlib.sha1(bs).hexdigest()}))
		self.assertEqual('bfb7759a67daeb65410490b4d98bb9da7d1ea2ce', res["sha1"])

	def test_iter_hash_raises_valueerror(self):
		with self.assertRaises(TypeError):
			dict(hashing.iterHash("lorem ipsum", struct={"sha1": lambda bs: hashlib.sha1(bs).hexdigest()}))

	def test_generate_hashlist(self):
		random_strings = map(partial(bytes, encoding="ascii"), util.generate_random_ascii(300))
		res = pd.DataFrame(hashing.createList(random_strings))
		self.assertEqual(300, len(res.index))
		self.assertTrue("crc32" in res.columns)
		self.assertTrue("name" in res.columns)
