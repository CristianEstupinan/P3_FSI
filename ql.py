import random
import numpy as np
import matplotlib.pyplot as plt


# Environment size
width = 5
height = 16

# Actions
num_actions = 4

actions_list = {"UP": 0,
                "RIGHT": 1,
                "DOWN": 2,
                "LEFT": 3
                }

actions_list_inverso = {0: "UP",
                        1: "RIGHT",
                        2: "DOWN",
                        3: "LEFT",
                        }

actions_vectors = {"UP": (-1, 0),
                   "RIGHT": (0, 1),
                   "DOWN": (1, 0),
                   "LEFT": (0, -1)
                   }

# Discount factor
discount = 0.8

Q = np.zeros((height * width, num_actions))  # Q matrix
Rewards = np.zeros(height * width)  # Reward matrix, it is stored in one dimension


def getState(y, x):
    return y * width + x


def getStateCoord(state):
    return int(state / width), int(state % width)


def getActions(state):
    y, x = getStateCoord(state)
    actions = []
    if x < width - 1:
        actions.append("RIGHT")
    if x > 0:
        actions.append("LEFT")
    if y < height - 1:
        actions.append("DOWN")
    if y > 0:
        actions.append("UP")
    return actions


def getRndAction(state):
    return random.choice(getActions(state))


def getRndState():
    return random.randint(0, height * width - 1)


Rewards[4 * width + 3] = -10000
Rewards[4 * width + 2] = -10000
Rewards[4 * width + 1] = -10000
Rewards[4 * width + 0] = -10000

Rewards[9 * width + 4] = -10000
Rewards[9 * width + 3] = -10000
Rewards[9 * width + 2] = -10000
Rewards[9 * width + 1] = -10000

Rewards[3 * width + 3] = 100
final_state = getState(3, 3)

#print np.reshape(Rewards, (height, width))


def qlearning(s1, a, s2):
    Q[s1][a] = Rewards[s2] + discount * max(Q[s2])
    return



# CALCULO PROMEDIO EXPLORACION

print "Exploracion: "

contadorExploracion = 0
contadorPorEpisodio = 0
vectorExploracion = []
numeroEpisodios = 1000

# Episodes
for i in xrange(numeroEpisodios):
    state = getRndState()
    while state != final_state:
        action = getRndAction(state)
        y = getStateCoord(state)[0] + actions_vectors[action][0]
        x = getStateCoord(state)[1] + actions_vectors[action][1]
        new_state = getState(y, x)
        qlearning(state, actions_list[action], new_state)
        state = new_state
        contadorExploracion = contadorExploracion + 1
        contadorPorEpisodio += 1
    vectorExploracion.append(contadorPorEpisodio)
    contadorPorEpisodio = 0

print "Calculo promedio:"
print contadorExploracion/numeroEpisodios
#print Q

# CALCULO PROMEDIO GREEDY

print "Greedy: "

Q = np.zeros((height * width, num_actions))
contadorGreedy = 0
contadorPorEpisodio = 0
vectorGreedy = []
numeroEpisodios = 1000

# Episodes
for i in xrange(numeroEpisodios):
    state = getRndState()
    while state != final_state:
        if max(Q[state]) != 0:
            indice = np.argmax(Q[state])
            action = actions_list_inverso[indice]
        else:
            action = getRndAction(state)
        y = getStateCoord(state)[0] + actions_vectors[action][0]
        x = getStateCoord(state)[1] + actions_vectors[action][1]
        new_state = getState(y, x)
        qlearning(state, actions_list[action], new_state)
        state = new_state
        contadorGreedy += 1
        contadorPorEpisodio +=1
    vectorGreedy.append(contadorPorEpisodio)
    contadorPorEpisodio = 0
print "Calculo promedio:"
print contadorGreedy/numeroEpisodios
#print Q

# CALCULO PROMEDIO E-GREEDY e=0.9

print "E-Greedy e=0.9: "

Q = np.zeros((height * width, num_actions))
contadorEGreedy09 = 0
contadorPorEpisodio = 0
vectorEGreedy09 = []
numeroEpisodios = 1000
e = 0.90


# Episodes
for i in xrange(numeroEpisodios):
    state = getRndState()
    while state != final_state:
        if max(Q[state]) != 0:
            if (random.random() > e):
                action = getRndAction(state)
            else:
                indice = np.argmax(Q[state])
                action = actions_list_inverso[indice]
        else:
            action = getRndAction(state)
        y = getStateCoord(state)[0] + actions_vectors[action][0]
        x = getStateCoord(state)[1] + actions_vectors[action][1]
        new_state = getState(y, x)
        qlearning(state, actions_list[action], new_state)
        state = new_state
        contadorEGreedy09 = contadorEGreedy09 + 1
        contadorPorEpisodio += 1
    vectorEGreedy09.append(contadorPorEpisodio)
    contadorPorEpisodio = 0

print "Calculo promedio:"
print contadorEGreedy09/numeroEpisodios
#print Q

# CALCULO PROMEDIO E-GREEDY e=0.85

print "E-Greedy e=0.85: "

Q = np.zeros((height * width, num_actions))
contadorEGreedy085 = 0
contadorPorEpisodio = 0
vectorEGreedy085 = []
numeroEpisodios = 1000
e = 0.85


# Episodes
for i in xrange(numeroEpisodios):
    state = getRndState()
    while state != final_state:
        if max(Q[state]) != 0:
            if (random.random() > e):
                action = getRndAction(state)
            else:
                indice = np.argmax(Q[state])
                action = actions_list_inverso[indice]
        else:
            action = getRndAction(state)
        y = getStateCoord(state)[0] + actions_vectors[action][0]
        x = getStateCoord(state)[1] + actions_vectors[action][1]
        new_state = getState(y, x)
        qlearning(state, actions_list[action], new_state)
        state = new_state
        contadorEGreedy085 = contadorEGreedy085 + 1
        contadorPorEpisodio += 1
    vectorEGreedy085.append(contadorPorEpisodio)
    contadorPorEpisodio = 0

print "Calculo promedio:"
print contadorEGreedy085/numeroEpisodios
#print Q

# CALCULO PROMEDIO E-GREEDY e=0.8

print "E-Greedy e=0.8: "

Q = np.zeros((height * width, num_actions))
contadorEGreedy08 = 0
contadorPorEpisodio = 0
vectorEGreedy08 = []
numeroEpisodios = 1000
e = 0.8


# Episodes
for i in xrange(numeroEpisodios):
    state = getRndState()
    while state != final_state:
        if max(Q[state]) != 0:
            if (random.random() > e):
                action = getRndAction(state)
            else:
                indice = np.argmax(Q[state])
                action = actions_list_inverso[indice]
        else:
            action = getRndAction(state)
        y = getStateCoord(state)[0] + actions_vectors[action][0]
        x = getStateCoord(state)[1] + actions_vectors[action][1]
        new_state = getState(y, x)
        qlearning(state, actions_list[action], new_state)
        state = new_state
        contadorEGreedy08 = contadorEGreedy08 + 1
        contadorPorEpisodio += 1
    vectorEGreedy08.append(contadorPorEpisodio)
    contadorPorEpisodio = 0

print "Calculo promedio:"
print contadorEGreedy08/numeroEpisodios

# Q matrix plot

s = 0
ax = plt.axes()
ax.axis([-1, width + 1, -1, height + 1])

for j in xrange(height):

    plt.plot([0, width], [j, j], 'b')
    for i in xrange(width):
        plt.plot([i, i], [0, height], 'b')

        direction = np.argmax(Q[s])
        if s != final_state:
            if direction == 0:
                ax.arrow(i + 0.5, 0.75 + j, 0, -0.35, head_width=0.08, head_length=0.08, fc='k', ec='k')
            if direction == 1:
                ax.arrow(0.25 + i, j + 0.5, 0.35, 0., head_width=0.08, head_length=0.08, fc='k', ec='k')
            if direction == 2:
                ax.arrow(i + 0.5, 0.25 + j, 0, 0.35, head_width=0.08, head_length=0.08, fc='k', ec='k')
            if direction == 3:
                ax.arrow(0.75 + i, j + 0.5, -0.35, 0., head_width=0.08, head_length=0.08, fc='k', ec='k')
        s += 1

    plt.plot([i+1, i+1], [0, height], 'b')
    plt.plot([0, width], [j+1, j+1], 'b')

plt.show()

plt.figure()
print vectorExploracion
vectorExploracion = np.array(vectorExploracion)
plt.plot(vectorExploracion)
plt.show()

plt.figure()
print vectorGreedy
vectorGreedy = np.array(vectorGreedy)
plt.plot(vectorGreedy)
plt.show()

plt.figure()
print vectorEGreedy09
vectorEGreedy09 = np.array(vectorEGreedy09)
plt.plot(vectorEGreedy09)
plt.show()

plt.figure()
print vectorEGreedy085
vectorEGreedy085 = np.array(vectorEGreedy085)
plt.plot(vectorEGreedy085)
plt.show()

plt.figure()
print vectorEGreedy08
vectorEGreedy08 = np.array(vectorEGreedy08)
plt.plot(vectorEGreedy08)
plt.show()