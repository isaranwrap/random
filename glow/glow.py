## How to create glowing neon effect in Python


# Glowing is really just dimishing the brightness/transparence outwards from the line

#Imports
import pandas as pd
import matplotlib.pyplot as plt

colors = [
    '#08F7FE',  # teal/cyan
    '#FE53BB',  # pink
    '#F5D300',  # yellow
    '#00ff41', # matrix green
]

fig, ax = plt.subplots()
creatB = [1.1, 1.1, 1, 1, 1.3, 1.3]
timeB =  [-8, -3, -2, 0, 2, 10]

creatD = [2, 2, 1, 1, 1, 4/3, 4/3, 5/3, 5/3]
timeD = [-8, -7, -2, 0, 0.5, 1, 5, 6, 10]

## PREVIOUS METHOD (PLAIN) ##
ax.plot(timeB, creatB)
ax.set_xlabel('time (days)')
ax.set_ylabel('creatinine (mg/dL)')
ax.set_title('Patient B')
ax.fill_between(timeB, creatB, 1, color='lightblue')

## NEW METHOD (GLOWY EFFECT) ##

# Darker style works well with neon blend
plt.style.use("seaborn-dark")
for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#2A3459'  # bluish dark grey
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light grey
ax.grid(color='#212946')  # bluish dark grey, but slightly lighter than background
ax.set_facecolor(color='#2A3459')

# Style alone:
fig, ax = plt.subplots(figsize=(12,9))
ax.plot(timeB, creatB, color=colors[0], label='B', marker='o')
ax.plot(timeD, creatD, color=colors[1], label='D', marker='o')
ax.legend()

# Neon effect:
draws = 10 # How many times to draw the line
diff_linewidth = 1.05 # Different line widths each draw
alpha_value = 0.03 # Alpha values of glow effect
glow_size = 5 # Glow linewidth

fig, ax = plt.subplots(figsize=(12,9))
ax.plot(timeB, creatB, alpha = 1.0, linewidth=2.0, color = colors[0], marker = 'o') # Plot the lines
ax.plot(timeD, creatD, alpha = 1.0, linewidth=2.0, color = colors[1], marker = 'o')
for n in range(draws): # Coat the lines in "glow" by drawing n lines around it

    ax.plot(timeB, creatB, color = colors[0],
            linewidth=glow_size+(diff_linewidth*n),
            alpha=alpha_value)
            
    ax.plot(timeD, creatD, color = colors[1],
            linewidth=glow_size+(diff_linewidth*n),
            alpha=alpha_value)

#ax.fill_between(time, creat, 1, color='orange')