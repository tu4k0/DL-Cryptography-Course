import hashlib


def SHA1_lib(message):
    sha1_object = hashlib.sha1(message.encode())
    sha1_hash = sha1_object.hexdigest()

    return sha1_hash
