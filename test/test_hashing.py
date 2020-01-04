import hashlib
from unittest import TestCase
from wrangleHash import hashing


class TestGenerateHashList(TestCase):
	def test_iter_hash(self):
		res = dict(hashing.iterHash(b"lorem ipsum", struct={"sha1": lambda bs: hashlib.sha1(bs).hexdigest()}))
		self.assertEqual('bfb7759a67daeb65410490b4d98bb9da7d1ea2ce', res["sha1"])

	def test_iter_hash_raises_valueerror(self):
		with self.assertRaises(TypeError):
			res = dict(hashing.iterHash("lorem ipsum", struct={"sha1": lambda bs: hashlib.sha1(bs).hexdigest()}))
