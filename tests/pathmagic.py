import os
import sys


class context:
    def __enter__(self):
        path = os.path.join(os.path.dirname(__file__), "../galois")
        sys.path.append(path)

    def __exit__(self, *args):
        pass
