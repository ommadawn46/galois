# Galois

```
❯ python -m unittest discover tests

GaloisField[59557] is Structure.FIELD

PolynomialRing[GaloisField[59557]] is Structure.INTEGRAL_DOMAIN

GaloisField[a^8 + a^4 + a^3 + a^2 + 1] is Structure.FIELD

PolynomialRing[GaloisField[a^8 + a^4 + a^3 + a^2 + 1]] is Structure.INTEGRAL_DOMAIN

PolynomialRing[int] is Structure.INTEGRAL_DOMAIN

BitsGaloisField is Structure.FIELD

MatrixRing is Structure.RING

MatrixMultiGroup is Structure.GROUP

ECPoint[y*y = x**3 + -2*x + 1] is Structure.ABELIAN_GROUP
.
CRC8(b'123456789') = b'\xf4'

CRC16_CCITT-FALSE(b'123456789') = b')\xb1'

CRC16_ARC(b'123456789') = b'\xbb='

CRC32(b'123456789') = b'\xcb\xf49&'

CRC32_Bzip2(b'123456789') = b'\xfc\x89\x19\x18'
.
x = 37365069129404004477355228029206881522913302440649915399590585058751015959404
P = {x: 98833230256033631612043916900993424385537650047314480243219594696057543238228, y: 64809687461837193960425278580914449615949883733787524164118079817927127361417}
m = b'This is a test message.'

elgamal.encrypt(m, P) = (c1, c2)
c1 = {x: 40279081884263036297254016857047020329340519825956480796972254293892529105225, y: 78698048017083408332565262243523202735676235158948207778708501130615848915671}
c2 = {x: 2810516866048067748609372309895516215801765835806363899084723866445150046061, y: 29163232413195196482076166991979066109040009368193049805106366279761825953086}
elgamal.decrypt(c1, c2, x) = b'This is a test message.'

elgamal.encrypt(m, P) = (c1_, c2_)
c1_ = {x: 74254378070419243233204863899521441007435647964806881709523335169554462273963, y: 15705211897928423564806342635528941090846633881467499579832611009614292026957}
c2_ = {x: 54636115600469266532943249216384460770472559771897510769838259988627622300817, y: 108515005586595127455045808007368765491174806324880562242732832131936510249874}
elgamal.decrypt(c1_, c2_, x) = b'This is a test message.'

(c1, c2) != (c1_, c2_)
.
NaiveRS.encode(b'Puzzle') = BitsRS.encode(b'Puzzle') = b'Puzzle\x84\x19\xee_'

NaiveRS.encode(b'Blackjack') = BitsRS.encode(b'Blackjack') = b'Blackjack\x9c\x99\x9c{\xe9[_\xb4sS\xcc\xa7S\x89h\xd8\xde'

NaiveRS.encode(b'ReedSolomonEncoding') = BitsRS.encode(b'ReedSolomonEncoding') = b'ReedSolomonEncoding\x86\xbd\xe8h\x84 Y'
.
NaiveRS.decode(b'Puzule\x84\x19\xed_') = b'Puzzle'

NaiveRS.decode(b'Blackjacb\x9c\x8e\x9cf\xe9[Y\xb5sF\xcd\xa7S\x89\xd5\xd8\xde') = b'Blackjack'

NaiveRS.decode(b'\xbdeedSolomonEnc\xacding\x86\xbd\xe8h\x84 Y') = b'ReedSolomonEncoding'

BitsRS.decode(b'H\x90 \xdaas an old man who fished alone in \xe0 skiff in \x92he Gu\x85f St\xd3Z+\xde\x006|F\xb5\x06\x93s\xbe\xa8\xbd\x16\x18\x99\xac}\xc6\xd56y3A\xb9\x07c\x9aD*\\]g#8\xdc\x0b\x8e') = b'He was an old man who fished alone in a skiff in the Gulf St'

BitsRS.decode(b're\x88m an\xb6 he had gone eighty-four d\rys now witho\x1ct \xd9aYing a fish. In the\rfirst\xfcforty days a boy had been with him. Bu\xef\xfbaf\x10[\xc9\xd7=\x01\xaa\xae\x17\xdb\xd36\xbd\xf5\xe3rk{w\x9di\xee\xb6Iv\xc5Wz\xe8\xdb') = b'ream and he had gone eighty-four days now without taking a fish. In the first forty days a boy had been with him. But af'

BitsRS.decode(b"ter >or\xa7y d\xa5ys wi\x15hour a fish th6 boy's p\x14rent\x90\xb1had told him thah th\x82 \x9f=d man wa\x9c now d>fini\xa0ely\xcbak\x91 f\xb2nallywsalao, ghich is the w\xdbrst form of unluckyl and the \x9aoy had go\\\xa6 at theiR&\x08x\xcf4A\x1a\xac\xfc\xde\xb4w\xcc\x80+j\xa7\x99BI\xa0L\xb5{m\x91\xe2\x10~\xe7n\xf7\xee\xc5>\xc4\xe1E\xebk\xfb+\xee\xfc\xf4\x8fj\xff&[\xfd\x94S\xad\r>\x94\x16\x9f\x0b\xfd\n\t\x95\x10\x1b^\xb9\x8d") = b"ter forty days without a fish the boy's parents had told him that the old man was now definitely and finally salao, which is the worst form of unlucky, and the boy had gone at thei"

ModuloRS.decode(b'The olJ man 8a6 !hin and1g|unty-Y\x83mh[5Fr0Me<w#A>;(\x83@B74gHnT.p+`#') = b'The old man was thin and gaunt'

ModuloRS.decode(b'wits ~eep\\wrinkl+sein the beckn\x82`6erQ9u<<X9NMGYL?CEpZXeR83[Xk\\+l\x81g3\\)#@d') = b'with deep wrinkles in the back'

ModuloRS.decode(b"of#uis ne<k. ThG trowY ._dtcax[8W.rb(AZ()hQr\x7fy\\z\x7f[xvNo()+\x83K3':6D5\x7f4qHsey\x84,XvibxY") = b'of his neck. The brown blotche'
.
----------------------------------------------------------------------
Ran 5 tests in 5.319s

OK
```
