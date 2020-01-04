import random
import string
from typing import Sequence


def generate_random_ascii(n: int, length: int = 15, char_class: Sequence[chr] = string.ascii_letters) -> Sequence[str]:
	return ["".join(random.choice(char_class) for i in range(length)) for x in range(n)]
