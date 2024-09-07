import numpy as np
import matplotlib.pyplot as plt

lahetettySymboli = complex(1,1)

kanavanImpulssivaste = complex(7, 0.2)

demoduloituSymboli = lahetettySymboli*kanavanImpulssivaste

'''
 Kanava kääntää vaihetta ja vaimentaa (tai vahvistaa) signaalin amplitudia
 Vaihe saadaan korjattua kanavan impulssivasteen kompleksikonjugaatilla kertoen
 Vihje: käytä np.conj komentoa

 Kanavan vaimennus saadaan kompensoitua jakamalla impulssivasteen itseisarvon neliöllä
 Vihje: käytä np.abs ja np.power komentoja

 Sinun tehtävänäsi on siis avata alla olevat kommentit ja kehittää oikea koodi ??? merkeillä
 merkattuihin kohtiin siten, että vaikka muuttelet miten tuota kanavan impulssivastetta, niin
 vaihe- ja amplitudikorjattu signaali palautuu aina lahetettySymboli muotoon.

'''

Vaihekorjattu = demoduloituSymboli * np.conj(kanavanImpulssivaste)
print("Vaihekorjattu signaali = ",Vaihekorjattu)

AmplitudiKorjattu = Vaihekorjattu / np.abs(np.power(kanavanImpulssivaste,2))
print("Vaihe ja amplitudikorjattu signaali = ", AmplitudiKorjattu)
print("")

'''
Ja toisena tehtävänä tutkitaan miten MIMO signaali voidaan vastaanottaa.
Tarvitaan siis tieto millaista kanavaa pitkin signaali on edennyt:
- Antennista 1 antenniin 1 => kanavanImpulssivaste h11
- Antennista 1 antenniin 2 => kanavanImpulssivaste h12
- Antennista 2 antenniin 1 => kanavanImpulssivaste h21
- Antennista 2 antenniin 2 => kanavanImpulssivaste h22

Tiedetään vain se mitä on vastaanotettu eli demoduloidut symbolit
- Mitä on vastaanotettu antennista 1 => r1
- Mitä on vastaanotettu antennista 2 => r2

Halutaan tietää mitä on lähetetty:
- Antennista 1 => s1
- Antennista 2 => s2

Lähetetään antennista 1 symboli 1+j ja antennista 2 2+2j,
Keksitään kanavan impulssivasteet ja lasketaan vastaanotetut symbolit, jotka
sitten korjataan (tai ratkaistaan yhtälöparista)
'''

l1 = complex(1,1)
l2 = complex(2,2)
h11 = complex(np.random.randn(1),np.random.randn(1))  # alustetaan kanava satunnaisesti
h12 = complex(np.random.randn(1),np.random.randn(1))  # alustetaan kanava satunnaisesti
h21 = complex(np.random.randn(1),np.random.randn(1))  # alustetaan kanava satunnaisesti
h22 = complex(np.random.randn(1),np.random.randn(1))  # alustetaan kanava satunnaisesti
#h11 = complex(1,1)
#h12 = complex(0.5,0.5)
#h21 = complex(-0.5,-0.5)
#h22 = complex(1,0.2)


# Laitetaan kaikki matriisimuotoon
print("")
L = np.array([[l1],[l2]])

print("lähetetty = ", L)
print("")

H = np.array([[h11,h12],[h21,h22]])
print("kanavamatriisi = ", H)

iH = np.linalg.inv(H)
print("käännetty kanavamatriisi = ", iH)

R = np.matmul(H,L)
print("Kanavalta vastaanotetaan = ", R)

print("")
K = np.matmul(iH,R)
print("kanavamatriisilla korjattu = ", K)


