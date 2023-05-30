def SHA1(message):
    def rotl(x, n):
        return ((x << n) | (x >> (32 - n))) & 0xffffffff

    h0 = 0x67452301
    h1 = 0xefcdab89
    h2 = 0x98badcfe
    h3 = 0x10325476
    h4 = 0xc3d2e1f0
    message_length = len(message.encode('utf-8')) * 8

    if 0 <= message_length < 2 ** 64:
        binary_string = ''.join(format(ord(i), '08b') for i in message)
        padded_message = binary_string + '1'
        k = 448 - (message_length + 1)
        padded_message += '0' * k
        end_message = 64 - message_length.bit_length()
        padded_message += '0' * end_message
        padded_message += bin(message_length)[2:]
        N = []
        M = []
        y = 0
        x = 0

        if len(padded_message) > 512:
            for i in range(0, len(padded_message) // 512):
                N.append(padded_message[x:x + 512])
                x += 512
        else:
            N.append(padded_message)
        for i in N:
            for j in range(0, 16):
                M.append(i[y:y + 32])
                y += 32
            for k in range(16, 80):
                M.append(rotl(int(M[k - 3], 2) ^ int(M[k - 8], 2) ^ int(M[k - 14], 2) ^ int(M[k - 16], 2), 1))
                M[k] = "{0:b}".format(M[k]).zfill(32)

        a = int(hex(h0), 16)
        b = int(hex(h1), 16)
        c = int(hex(h2), 16)
        d = int(hex(h3), 16)
        e = int(hex(h4), 16)

        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = int('0x5A827999', 16)
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = int('0x6ED9EBA1', 16)
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = int('0x8F1BBCDC', 16)
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = int('0xCA62C1D6', 16)

            M[i] = int(hex(int(M[i], 2)), 16)
            T = rotl(a, 5) + f + e + k + M[i] & 0xffffffff
            e = d
            d = c
            c = rotl(b, 30)
            c = int("{0:b}".format(c).zfill(64)[32:64], 2)
            b = a
            a = T

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

        sha1_hash = '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

        return sha1_hash



