import matplotlib.pyplot as plt
import numpy as np

# Transformation matrix
T = np.array([
              [1,.5],
              [0,.5]
            ])


# define the set of points (a circle)
theta = np.linspace(0,2*np.pi-2*np.pi/20,20)
origPoints = np.vstack( (np.cos(theta),np.sin(theta)) )

# apply transformation
transformedPoints = T @ origPoints


# plot the points
plt.figure(figsize=(6,6))
plt.plot(origPoints[0,:],origPoints[1,:],'ko',label='Original')
plt.plot(transformedPoints[0,:],transformedPoints[1,:],'s',
         color=[.7,.7,.7],label='Transformados')

plt.axis('square')
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.legend()
#plt.savefig('Figure_07_08.png',dpi=300)
plt.show()