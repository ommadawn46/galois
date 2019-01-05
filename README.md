# Galois

```
❯ python -m unittest discover tests

GaloisField[39733] is Structure.FIELD

PolynomialRing[GaloisField[39733]] is Structure.INTEGRAL_DOMAIN

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
NaiveRS.encode(b'Puzzle') = BitsRS.encode(b'Puzzle') = b'Puzzle\x84\x19\xee_'

NaiveRS.encode(b'Blackjack') = BitsRS.encode(b'Blackjack') = b'Blackjack\x9c\x99\x9c{\xe9[_\xb4sS\xcc\xa7S\x89h\xd8\xde'

NaiveRS.encode(b'ReedSolomonEncoding') = BitsRS.encode(b'ReedSolomonEncoding') = b'ReedSolomonEncoding\x86\xbd\xe8h\x84 Y'
.
NaiveRS.decode(b'Puztld\x84\x19\xee_') = b'Puzzle'

NaiveRS.decode(b'Blacksack\x9d\xc2\x9c{\xe9[_\xbas\xfb\xcc\xa5S\x89\xe9\xd8\xde') = b'Blackjack'

NaiveRS.decode(b'ReddSoldmonEnc}ding\x86\xbd\xe8h\x84 Y') = b'ReedSolomonEncoding'

BitsRS.decode(b'H\x8f was an old man who fished alone \xbdn a \xfdki\xebf in the Gu\xa9f St\xf8 +\xde\x006\xc9>\x0f\x06\x93\xcb\xbe\xa8\xbd\x16\xf0\x99\xac\x02\xf9\xd56\x18\x89A-\x8ec\x9ar9.]g#\n\xdc\x0b\xe8') = b'He was an old man who fished alone in a skiff in the Gulf St'

BitsRS.decode(b'ream\xd6a;d he had goHe\xb8eighty-fou\xf8 d\xf8ys \x83ow wit\xd9out \x8aaking a fish. In the first \x8fo\xc8ty days a boy had been\x0ewith\x05him. \xc3ut af\xb1[\xc9\xd7=\x01\xaa\xaei\xdb\xd3Q\xbd\xf5\xe3rk{w\x9d\x10\xee\xb6Iv\xf5Wzl\xdb') = b'ream and he had gone eighty-four days now without taking a fish. In the first forty days a boy had been with him. But af'

BitsRS.decode(b"ter forty\x11days witHout a;\x91ish t)e*boy's\xd5parent\xa4 had t`ld him Zhat the old \x81a\xf7 was no/ defi\xf2itewy6\xfand fin!lly salao,\xafw2Mch*is the worst\xa5form of unlucky, and the boy had go\xade a\xe6\x11the\xfcR&\x08x\xcf\x12A\x1a\xac\xfc\xde\xa7\xf85\x80+j\xa7}BI\xa0L\xb5{m\x91\xd8\x10~@n\xf7\xee\xc5>\xc4\xebE\xebk\xfb8\xee\xfc\xf4\x8fj\xff&[\xfd\x18\xe8\xad\r>\x94\x16\x9f\x0b\xfd\n\t\x95\x10\x1b^\xa9\x01") = b"ter forty days without a fish the boy's parents had told him that the old man was now definitely and finally salao, which is the worst form of unlucky, and the boy had gone at thei"

ModuloRS.decode(b'1he oOd m}nrwas5thinTaPU gauntyhB)mh`5Fr0Me<"#"w;9 @17UgSnv.]h`7') = b'The old man was thin and gaunt'

ModuloRS.decode(b"with djip wrin(leM ig -he backn\\`6h%E`u<<BUx!GY4A6ppZXXR83[`v\\+'#gTmA#1\x80") = b'with deep wrinkles in the back'

ModuloRS.decode(b'of his nee;.=Thecbro}" blothhe[$Wy{Y(A^(L!Q~-U\\zC[uvND()+\x83K3re%\x7f5\x7fBqHse^\x84,X#]Exn') = b'of his neck. The brown blotche'
.
----------------------------------------------------------------------
Ran 4 tests in 4.326s

OK
```
