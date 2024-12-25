import numpy as np
import matplotlib.pyplot as plt

# Creating the grids

x = np.linspace(-10,10,200)
y = np.linspace(-10,10,200)

X , Y = np.meshgrid(x,y)

# Initializing the velocity components
u = -1 - X**2 + Y
v = 1 + X - Y**2

# calculating the velocity magnitude
vel_mag = np.sqrt(u**2 + v**2)


#plotting

plt.figure(figsize=(10,10))
plt.streamplot(X,Y,u,v,color=vel_mag)
plt.colorbar(label = 'VELOCITY MAGNITUDE')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.title('streamlined Plot')
plt.show()

