def pack_bin_list(bin_list, revese=False):
    out = "".join(map(lambda x: str(x), bin_list[::-1]))
    pad = len(out) % 8
    out = "0" * (8 - pad if pad else 0) + out
    byte_n = len(out) // 8

    if revese:
        out = out[::-1]
    out_data = int(out, 2).to_bytes(byte_n, "big")
    if revese:
        out_data = out_data[::-1]
    return out_data


def unpack_data(byte_data, revese=False):
    bin_list = []
    for b in byte_data:
        word_bin = []
        for i in range(8):
            word_bin.append(b % 2)
            b //= 2
        if revese:
            word_bin = word_bin[::-1]
        bin_list = word_bin + bin_list
    return bin_list


def bin_to_byte(bin_list):
    return [bin_list[i * 8 : (i + 1) * 8] for i in range(len(bin_list) // 8)]
