from random import randrange

# Reservoir Sampling
# p(a) = 1/n
# not p(a) = (1-1/n)

# for single element
# p(ai) = [1/i] [1 - 1/(i+1)] [1 - 1/(i+2)] ...... [1 - 1/n]
# p(ai) = [1/i] [i/i+1] [i+1/i+2] [i+2/i+3] ........[n-1/n]
# p(ai) = [1/n] V elements in stream

# for k elements
# p(ai) = [k/i] [1 - 1/(i+1)] [1 - 1/(i+2)] ...... [1 - 1/n]
# p(ai) = [1 - 1/(i+1)] [1 - 1/(i+2)] ...... [1 - 1/n]
# p(ai) = [k/n] V elements in stream


def reservoirSampling(stream, n, k):
    
    choosen = [stream[i] for i in range(k)]

    for i in range(k, n):
        # pick a number random in range(0,i+1)
        pick = randrange(i+1)
        # check if chosen
        if pick < k:
            choosen[pick] = stream[i]

    return choosen

# checking with Monte Carlo principle
def simulate(simulationCount, k, n):

    probCount = [0 for i in range(20)]
    prob = k/float(n)
    for count in range(simulationCount):
        choosen = reservoirSampling(arr, len(arr), k)
        for num in range(20):
            if num in choosen:
                probCount[num]+= 1
    print(f"Simulation for {simulationCount}")
    print(f"Expected probability {prob}\n\n")
    for i in range(20):
        pofi = probCount[i]/float(simulationCount)
        print(f"Probability of {i} is {pofi}")
    
if __name__ == "__main__":
    arr = list(range(20))
    k = 5
    simulate(100000, k, 20)
