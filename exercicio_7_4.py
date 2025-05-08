import matplotlib.pyplot as plt
import numpy as np

# Configuração da animação
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')

# função para desenhar a plotagem no gráfico
def aframe(ph):
  # cria a matriz de transformação
  A = np.array([ [  1-ph/3,0 ], [  0,ph   ] ])
  # aplica a transformação dos pontos usando a matriz de transformação
  P1 = A @ Y1
  P2 = A @ Y2

  # atualiza as linhas inferiores e superiores
  plth1.set_xdata(P1[0,:])
  plth1.set_ydata(P1[1,:])
  plth2.set_xdata(P2[0,:])
  plth2.set_ydata(P2[1,:])
  # exporta os manipuladores da plotagem
  return (plth1,plth2)

# define os pontos X e Y
theta = np.linspace(0,2*np.pi,100) # theta (ângulos)
Y1 = np.vstack((theta,np.cos(theta)))
Y2 = np.vstack((theta,np.sin(theta)))


# configura a figura
fig,ax = plt.subplots(1,figsize=(12,6))
# plotagem inicial
plth1, = ax.plot(Y1[0,:],Y1[1,:],'ko') # plota Cosseno de preta
plth2, = ax.plot(Y2[0,:],Y2[1,:],'s',color=[.7,.7,.7]) # plota Seno de cinza
ax.set_ylim([-2,2])


# define as fases e roda a animação
phi = 1-np.linspace(-1,1-1/40,40)**2
anim = animation.FuncAnimation(fig, aframe, phi, interval=50, repeat=True)

plt.show()


