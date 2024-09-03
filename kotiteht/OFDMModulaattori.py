import numpy as np
import matplotlib.pyplot as plt

taajuustaso = np.zeros((128),dtype=complex)
taajuustaso[3] = complex(2,2);  # Tässä on nyt moduloitu yksi alikantoaalto
# Moduloi tähän myös alikantoaallot 10 ja 30 QPSK-modulaatiota käyttäen
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