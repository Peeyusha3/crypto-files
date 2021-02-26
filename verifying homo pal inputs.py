import gmpy2
from gmpy2 import mpz
x1_t1=(gmpy2.mul(6.6398062446732355,6.163159303134653))
print(x1_t1)
x2_t2=(gmpy2.mul(6.904305754443274,5.487643787264671))
print(x2_t2)
x3_t3=(gmpy2.mul(5.590421405137484,4.381448384651916))
print(x3_t3)
inb=gmpy2.add(x1_t1,x2_t2)
inb2=gmpy2.add(inb,x3_t3)
inb3=gmpy2.add(inb2,3.1043289504033473)
print(inb3)