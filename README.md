# Attractor animations

This project generates animations for various mathematical [attractors](https://en.wikipedia.org/wiki/Attractor). The animations are currently created using Python, Numpy and the Matplotlib library. They should however be rewritten in something faster.

## How to use
1. Clone the repository
2. Run the file for the attractor you want
3. Animations will be saved as a GIF in the output directory

## Requirements
* Numpy
* Matplotlib

## Available attractors
* Halvorsen
$$
\begin{equation}
    \begin{cases}
        \frac{dx}{dt}=-a\cdot x-4\cdot y-4\cdot z-y\cdot y\\
        \frac{dy}{dt}=-a\cdot y-4\cdot z-4\cdot x-z\cdot z\\
        \frac{dy}{dt}=-a\cdot z-4\cdot x-4\cdot y-x\cdot x\\
    \end{cases}\,.
\end{equation}
$$
