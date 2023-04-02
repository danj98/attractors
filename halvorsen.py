import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Number of points
n = 10000
# Create initial point
x0, y0, z0 = (1, 0, 0)

a = 1.4
tmax = 100


# A single step for a Halvorsen attractor
def halvorsen(t, coords, a):
    x, y, z = coords
    x_new = -a * x - 4 * y - 4 * z - y ** 2
    y_new = -a * y - 4 * z - 4 * x - z ** 2
    z_new = -a * z - 4 * x - 4 * y - x ** 2

    return x_new, y_new, z_new


soln = solve_ivp(halvorsen, (0, tmax), (x0, y0, z0), args=(a,), dense_output=True)
interpolation = np.linspace(0, 1000, n)

x_upd = np.zeros(len(interpolation))
y_upd = np.zeros(len(interpolation))
z_upd = np.zeros(len(interpolation))

# Create 3d scatter plot
plt.style.use('dark_background')
fig = plt.figure(figsize=(10, 6), dpi=80)
ax = fig.add_subplot(projection="3d")

ax.view_init(30, -10)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False


# Function to update each coordinate every frame
def update_coordinates(i):
    x_upd[i] = soln.sol(interpolation).T[i][0]
    y_upd[i] = soln.sol(interpolation).T[i][1]
    z_upd[i] = soln.sol(interpolation).T[i][2]
    progress = (i / n) * 100
    print("Progress: {:.1f}%".format(progress))
    ax.clear()
    ax.view_init(30, -10 + i/4)
    ax.plot(x_upd[:i], y_upd[:i], z_upd[:i])

    ax.set_xticks([])
    ax.set_yticks([])
    ax.zaxis.line.set_lw(0.)
    ax.set_zticks([])

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])


# Setting axis properties
ax.set(xlim3d=(-10, 10), xlabel="X")
ax.set(ylim3d=(-10, 10), ylabel="Y")
ax.set(zlim3d=(-10, 10), zlabel="Z")


# Creating animation
ani = FuncAnimation(fig, update_coordinates, np.arange(n), interval=20, repeat=False)
print("100%%\nSaving animation")
ani.save("output/halvorsen.gif", dpi=300, writer="pillow", fps=50)
print("Done!")
