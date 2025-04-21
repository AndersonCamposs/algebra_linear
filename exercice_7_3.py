import matplotlib.pyplot as plt
import numpy as np

# Matriz de transformação
T = np.array([[1,.5], [0,.5]])


# Define o conjunto de pontos do círculo
theta = np.linspace(0,2*np.pi-2*np.pi/20,20)
pontos_originais = np.vstack( (np.cos(theta),np.sin(theta)) )



# Aplicada a tranformação do pontos originais com base na matriz de transformação
pontos_transformados = T @ pontos_originais


# Plota os pontos no gráfico
plt.figure(figsize=(6,6))
plt.plot(pontos_originais[0,:],pontos_originais[1,:],'ko',label='Pontos originais')
plt.plot(pontos_transformados[0,:],pontos_transformados[1,:],'s', color=[.7,.7,.7],label='Pontos transformados')

plt.axis('square')
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.legend()
#plt.savefig('Figure_07_08.png',dpi=300)
plt.show()