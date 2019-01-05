# Galois

```
❯ python -m unittest discover tests

GaloisField[45377] is Structure.FIELD

PolynomialRing[GaloisField[45377]] is Structure.INTEGRAL_DOMAIN

GaloisField[a^8 + a^4 + a^3 + a^2 + 1] is Structure.FIELD

PolynomialRing[GaloisField[a^8 + a^4 + a^3 + a^2 + 1]] is Structure.INTEGRAL_DOMAIN

PolynomialRing[int] is Structure.INTEGRAL_DOMAIN

BitsGaloisField is Structure.FIELD

MatrixRing is Structure.RING

MatrixMultiGroup is Structure.GROUP
.
CRC8(b'123456789') = b'\xf4'
CRC16_CCITT-FALSE(b'123456789') = b')\xb1'
CRC16_ARC(b'123456789') = b'\xbb='
CRC32(b'123456789') = b'\xcb\xf49&'
CRC32_Bzip2(b'123456789') = b'\xfc\x89\x19\x18'
.
BitsRS.decode(b'He wa\x0b an \x19ld man who fished a\xe6on\x1a in a skiff\x12in\x03tm- G\xdelf \xd0t\xd3\x1f{:\x006VF\x0f\x06\xfd\xcb\xbe\xa8\xbd\x82\x18\x99\xac}\xf9\xd56A3A\x05\x8ec\x9a\x9b\x96\\]g#X\xdc\x0b\x8e') = b'He was an old man who fished alone in a skiff in the Gulf St'
BitsRS.decode(b'ream an\xfb he had @one\xbfeig\xb3ty-four days \x87ow withou1 t\xa7king a fish. In the first fordB days a boy had be7n withJhim\x92 But af\xb1[\xc9\xd7=\x01\xaa\xaei\xdb\xd3B\xbd\xf5\xe3rk{w\xea\x10\xee\xb6Iv\xf5Wz)\xdb') = b'ream and he had gone eighty-four days now without taking a fish. In the first forty days a boy had been with him. But af'
BitsRS.decode(b"t\xc3r forty days without a fish the boy's par\x9c\x8bt\xa0 had t\xadld\x0ehim mhbt the old m&n wa\x99ynow definit\xe6ly and fi9ally salao, which is the wors\\ for\xf2 of unlu\xd3ky, and\x12the boy 38d\xd2goneMat theiR&\x08x\xcf3A\x1a\xac\xfc\xde\xa7w5\x80+j\xa7\x99*I\xa0\x8d\xb5{m\x91\xd8\x10~\xe7n\xf7\xee\xa6\x81\xc4\xebE\x91k\xfb+\xee\xfc\xf4\x8f\xf0\xff&[\xfd\x94\xac\xad\r>\x94\x16\x9f\x0b\xfd\x0f\t\x95\x10\x1b^\xa9W") = b"ter forty days without a fish the boy's parents had told him that the old man was now definitely and finally salao, which is the worst form of unlucky, and the boy had gone at thei"
.
NaiveRS.encode(b'Puzzle') = BitsRS.encode(b'Puzzle') = b'Puzzle\x84\x19\xee_'
NaiveRS.encode(b'Blackjack') = BitsRS.encode(b'Blackjack') = b'Blackjack\x9c\x99\x9c{\xe9[_\xb4sS\xcc\xa7S\x89h\xd8\xde'
NaiveRS.encode(b'ReedSolomonEncoding') = BitsRS.encode(b'ReedSolomonEncoding') = b'ReedSolomonEncoding\x86\xbd\xe8h\x84 Y'
.
ModuloRS.decode(b'Theqold ta1 Zaskthin and gpuWvy\x80"\x83mh[jFr0Me<p#"w;9\x83@u7PgSn[.)hW7') = b'The old man was thin and gaunt'
ModuloRS.decode(b"lioh #eep wNinkl0s in NheCba~^n>`6e%0`Z<<\x81UwMGY/A6ppLXec83IQk\\+'\x81gT/A#@\x80") = b'with deep wrinkles in the back'
ModuloRS.decode(b'Hf ti` neck. Thl brow6 blo0c.H[$W.g"9A^(L=K~Oy\'zC[#vgo()+\x83m3\':w[5\x7f%FH>ey\x84,3viEpY') = b'of his neck. The brown blotche'
.
NaiveRS.decode(b'Puz~l}\x84\x19\xee_') = b'Puzzle'
NaiveRS.decode(b'$lack>ac\xd4\x9c\x99\x9c{\xe9[_\xb4)5\xcc\xa7S\x89h\xd8\xf6') = b'Blackjack'
NaiveRS.decode(b'ReedSolmmonE\x0cpoding\x86\xbd\xe8h\x84 Y') = b'ReedSolomonEncoding'
.
----------------------------------------------------------------------
Ran 6 tests in 4.497s

OK
```
