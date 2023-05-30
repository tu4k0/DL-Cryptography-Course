import time
import tracemalloc

from Practice5.hashing_algorithms.SHA1_own import SHA1_own
from Practice5.hashing_algorithms.SHA1_lib import SHA1_lib


def main():
    message = input('Enter the message: ')
    print('-' * 100)
    sha1_own_start_time = time.perf_counter()
    tracemalloc.start()
    sha1_own_hash = SHA1_own(message)
    print('SHA1 hash of the message (Own implementation): ', sha1_own_hash)
    print('Hashing time: ', time.perf_counter() - sha1_own_start_time)
    print('Amount of used memory (current, peak): ', tracemalloc.get_traced_memory())
    tracemalloc.stop()
    print('-' * 100)
    sha1_lib_start_time = time.perf_counter()
    tracemalloc.start()
    sha1_lib_hash = SHA1_lib(message)
    print('SHA1 hash of the message (Hashlib implementation): ', sha1_lib_hash)
    print('Hashing time: ', time.perf_counter() - sha1_lib_start_time)
    print('Amount of used memory (current, peak): ', tracemalloc.get_traced_memory())
    tracemalloc.stop()


if __name__ == '__main__':
    main()
