import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


# au
# sampling information
Fs = 44100 # sample rate
T = 1/Fs # sampling period
t = 0.1 # seconds of sampling
N = Fs*t # total points in signal

# signal information
freq = 100 # in hertz, the desired natural frequency
omega = 2*np.pi*freq # angular frequency for sine waves

t_vec = np.arange(N)*T # time vector for plotting
y = np.sin(omega*t_vec)

plt.plot(t_vec,y)
plt.show()

np.fft.fft(y)

# transformée de fourier et domaine fréquentiel 
# 
Y_k = np.fft.fft(y)[ 0 : int (N/ 2 )]/N # Fonction FFT de numpy 
Y_k[ 1 :] = 2 *Y_k[ 1 :] # besoin de prendre le spectre unilatéral uniquement 
Pxx = np.abs(Y_k) # assurez-vous de vous débarrasser de la partie imaginaire

f = Fs*np.arange((N/ 2 ))/N; # vecteur de fréquence

# tracé
fig,ax = plt.subplots()
plt.plot(f,Pxx,linewidth= 5 )
ax.set_xscale( 'log' )
ax.set_yscale( 'log' )
plt.ylabel( 'Amplitude' )
plt.xlabel( 'Fréquence [Hz]' )
plt.show()