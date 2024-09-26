from matplotlib import pyplot as plt
import numpy as np


def plot_barb(wind_dir, wind_spd):
    if wind_dir == -1 and wind_spd == -1:
        raise ValueError("Wind direction and speed not provided, "
                         "no plot will be shown.")
    u = wind_spd * np.sin(np.radians(wind_dir))
    v = wind_spd * np.cos(np.radians(wind_dir))

    fig, ax = plt.subplots()

    if wind_spd < 5:
        color = 'lightgreen'
    elif 5 <= wind_spd < 10:
        color = 'green'
    elif 10 <= wind_spd < 15:
        color = 'blue'
    elif 15 <= wind_spd < 20:
        color = 'yellow'
    elif 20 <= wind_spd < 25:
        color = 'orange'
    else:
        color = 'red'

    ax.barbs(0, 0, u, v, length=15, pivot='middle', barbcolor=color,
             barb_increments=dict(half=5, full=10, flag=50), )
    ax.text(0.06, 0.04, f"{wind_spd} kts", color=color)
    ax.text(0.06, 0.03, f"{wind_dir}°", color='darkgreen')

    bearing = plt.Circle((0, 0), 0.05, color='black', fill=False)
    ax.add_artist(bearing)

    for angle in range(0, 360, 30):
        x = 0.05 * np.sin(np.radians(angle))
        y = 0.05 * np.cos(np.radians(angle))
        ax.plot([0, x], [0, y], color='black', linestyle='dotted')
        if angle == 0 and angle == 180:
            ax.text(x * 1, y * 1, f"{angle}°", color='black')
        elif 0 < angle < 180:
            ax.text(x * 1.05, y * 1.15, f"{angle}°", color='black')
        else:
            ax.text(x * 1.25, y * 1.15, f"{angle}°", color='black')

    ax.set_aspect('equal')

    for spine in ax.spines.values():
        spine.set_visible(False)
        ax.set_axis_off()

    plt.show()
# TODO: Add runway direction inquiry and plot runways as well
