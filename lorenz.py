import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import gc


def lorenz(coords, s=10, r=28, b=2.667):
    x, y, z = coords
    x_new = s * (y - x)
    y_new = x * (r - z) - y
    z_new = x * y - b * z
    return np.array([x_new, y_new, z_new])


dt = 0.01
num_steps = 10000

# Empty array for coordinates
coords = np.empty((num_steps + 1, 3))
# Initial values
coords[0] = (0., 1., 1.05)

# Calculate all the values
for i in range(num_steps):
    if i % 100 == 0:
        gc.collect()
    coords[i+1] = coords[i] + lorenz(coords[i]) * dt

# Create 3d scatter plot
plt.style.use('dark_background')
fig = plt.figure(figsize=(10, 6), dpi=80)
ax = fig.add_subplot(projection="3d")
ax.view_init(30, -10)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.set(xlim3d=(-10, 10), xlabel="X")
ax.set(ylim3d=(-10, 10), ylabel="Y")
ax.set(zlim3d=(-10, 10), zlabel="Z")


# Update animation
def update(i):
    ax.clear()
    ax.view_init(30, -10 + i/4)
    ax.scatter(coords[:i, 0], coords[:i, 1], coords[:i, 2])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.zaxis.line.set_lw(0.)
    ax.set_zticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])
    if i % 100 == 0:
        gc.collect()


ani = FuncAnimation(fig, update, np.arange(num_steps), interval=50, repeat=False)
ani.save("output/lorenz.gif", dpi=100, writer="pillow", fps=30)
