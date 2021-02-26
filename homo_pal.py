import gmpy2
import numpy
from gmpy2 import mpz
from random import randint

#Initialize
p = mpz(91384202109071442293463836021112242872202112556997233738650771115304627068435244189452217404518350934650625169787645878831492249234702966702870665364147218752886578786376766042770107058123323172961898496290467790495229761191517699758387645314555098976305458147233083947409856486295027584628343852346198294834673398056518565970306137057662042381108071850367597403128086501769091999204250111973206216989075174484334959172281822465253170809350903328437985069427319)
q = mpz(81461618609951926714232486073323681843605711813586129469089521881286578240351609211470308250561781558375310490543983933780038328473513066035201591085583608631590043360965785867067725207262314428957973642440166838678305658012018727393737744349209249924848069061992265051686526452564260097993214532057415090837113730859560081637862504223208931316591467688041729971515846931082731879867661935144206080893902297595573259652166808407688180529379028374251689469303983)
#m=mpz(randint(1,5000)) #randomly generated message
r=mpz(randint(1,4000)) #random number generated
n = gmpy2.mul(p,q) # n = p*q 
lamda = gmpy2.mul(p-1,q-1) #lambda = (p-1)*(q-1)
g = n+1 #special case
n2 = pow(mpz(n),2) #n^2
alice,bob,E=[],[],[] #lists used to store values as vector

#Encryption
def encryption(mes):
    c = gmpy2.powmod((gmpy2.mul(gmpy2.powmod(g,mes,n2),gmpy2.powmod(r,n,n2))),1,n2)# c = [(g^m mod n).(r^n mod n)])mod n^2
    return c

#Decryption
def decryption(ci):
    x = (gmpy2.powmod(ci,lamda,n2)) # x = (c^lamda mod n^2)
    s = gmpy2.powmod(mpz((x-1)//n),1,n) # S = L[(c^lamda mod n^2)-1/n] mod n
    m_obtained = gmpy2.powmod(gmpy2.mul(gmpy2.powmod(s,1,n),gmpy2.invert(lamda,n)),1,n) # m_obtained = (S modn * lamda^-1 modn) mod n
    return m_obtained

#printing I/O
print("Homooooo pallier")
print("The public-key (g, n) : ",g,"\n\n",n,"\n\n")
print("The private-key (λ, p, q) : ",lamda,"\n\n",p,"\n\n",q,"\n\n")
print("-------------------------------------------------------")
l=int(input("Please enter l(>=3) : "))
print("-------------------------------------------------------")

#taking x values for alice and printing
print("\nInput x for Alice (floating point numbers):")
for i in range(l):
    y=float(input("x["+str(i+1)+"]= "))
    alice.append(mpz(y*(2**30)//1))
print("Encoded x: ",alice)

#taking theta values for bob and printing
print("\nInput θ for Bob (floating point numbers):")
th0=float(input("Enter theta_0: "))
th0=mpz(th0*(2**60)//1)
for j in range(l):
    z=float(input("th["+str(j+1)+"]= "))
    bob.append(mpz(z*(2**30)//1))
print("Encoded θ: ",bob)
print("-------------------------------------------------------")

#encrypting x values on alice side and printing
for i in range(l):
    E.append(encryption(alice[i]))
print("\n Encrypted vector E(x)= ",E)

#E(f(x,theta))
for i in range(l):
    E[i]=gmpy2.powmod(E[i],bob[i],n2)
print("\n Encrpted result E(f(th,x))= ",E)
print("--------------------------------------------------------")
E_th0=encryption(th0) #encrypting E(theta)
E_enc=numpy.prod(E) #product of E vector
E_enc=gmpy2.mul(E_th0,E_enc) #product of E(xi) and E(theta)
print("\n Decrypted encoded result= ",E_enc)
m_ob=decryption(E_enc) #decrypting E(f(x,theta)) to get f(x,theta)
m_res=m_ob/(2**60) #dividing by 2**60
print("\n Decrypted result f(th,x)= ",m_res)
print("---------------------------------------------------------")

