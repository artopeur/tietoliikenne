import numpy as np
import matplotlib.pyplot as plt

taajuustaso = np.zeros((128),dtype=complex)
taajuustaso[3] = complex(2,2);  # Tässä on nyt moduloitu yksi alikantoaalto
# Moduloi tähän myös alikantoaallot 10 ja 30 QPSK-modulaatiota käyttäen
taajuustaso[10] = complex(2,2)
taajuustaso[30] = complex(2,2)
# Eli tarkoittaa siis sitä, että sinulla on käytettävissäsi 00 => 1+j, 11 => -1-j, 01 => -1+j ja 
# 10 => 1-j vaihtoehdot.

print(taajuustaso[:])

aikataso = np.fft.ifft(taajuustaso[:]);
print(aikataso.real)
print(aikataso.imag)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(aikataso.real)
plt.title('Moduloidun signaalin kosinihaara')
plt.subplot(2,1,2)
plt.plot(aikataso.imag)
plt.title('Moduloidun signaalin sinihaara')
plt.show()

# Ja tänne pitäisi opiskelijan sitten osata tehdä bittipäätökset
# Eli sinun pitää tulla aikatason signaalista takaisin taajuustasoon
# ja tehdä bittipäätökset alikantoaaltojen 3, 10, 30 osalta.

def decide(taajuus):
    I = np.real(taajuus)
    Q = np.imag(taajuus)
    vaihe = np.arctan2(Q, I)
    if vaihe > 0 and vaihe <= np.pi/2:
       bits = (0,1)
    elif vaihe > np.pi/2 and vaihe <= np.pi:
        bits = (0,0)
    elif vaihe > -np.pi and vaihe <= -np.pi/2:
        bits = (1,0)
    else:
        bits = (1,1)
    return bits

taajuust = np.fft.fft(aikataso)
bits = (0,0)
bits = decide(taajuust[3])
print("3: ", bits)
bits = decide(taajuust[10])
print("10: ", bits)
bits = decide(taajuust[30])
print("30: ", bits)
