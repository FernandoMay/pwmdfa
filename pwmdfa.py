import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 300  # Frecuencia de muestreo
f_audio = 100  # Frecuencia de la señal de audio
f_triangular = 1000  # Frecuencia de la señal triangular
t = np.linspace(0, 1, fs)

# Señal de audio (senoidal)
audio_signal = np.sin(2 * np.pi * f_audio * t)

# Señal triangular
triangular_signal = 2 * (t * f_triangular % 1) - 1

# Modulación PWM
pwm_signal = np.zeros_like(t)
for i in range(len(t)):
    pwm_signal[i] = 1 if audio_signal[i] > triangular_signal[i] else 0

# Visualización
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, audio_signal)
plt.title("Señal de Audio")
plt.subplot(3, 1, 2)
plt.plot(t, triangular_signal)
plt.title("Señal Triangular")
plt.subplot(3, 1, 3)
plt.plot(t, pwm_signal)
plt.title("Señal PWM")
plt.show()
