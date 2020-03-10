import random
import time
import matplotlib.pyplot as plt

def fitness(queens, printBool):
    if (printBool): print('Fighting Queens:')
    count = 0
    for i in range(0,8):
        for j in range(1,8-i):
            if (queens[i+j]==queens[i]+j 
                or queens[i+j]==queens[i]-j
                or queens[i] == queens[i+j]):
                count += 1
                if (printBool): print(count,': ',i+1,' and ',i+j+1,' fight')
    return (max((28-count),.01))

def printBoard(board):
    queens = board[1]
    print(board)
    if (v):
        notUsed = fitness(queens,v)
        print('pairs of non-fighting queens: ',(board[0]))
        print('\n   1 2 3 4 5 6 7 8')
        for i in range(0,8):
            print(i+1,' ',end='')
            for j in range(0,8):
                if queens[j]==i:
                    print('Q ',end='')
                else:
                    print('_ ',end='')
            print()
        print('\n')

def crossoverSpecimens(specA, specB):
    r = random.sample(range(0,8),1)[0]
    tempOne = specA[1][0:r] + specB[1][r:8]
    tempTwo = specB[1][0:r] + specA[1][r:8]
    return [0,tempOne],[0,tempTwo]

def mutateSpecimen(spec, mutPct):
    if (0): print('specimen in mutation function: ',spec)
    mutateBool = (mutPct * 100) >= random.sample(range(0,100),1)[0]
    if (mutateBool):
        r = random.sample(range(0,8),1)[0]
        m = random.sample(range(0,8),1)[0]
        spec[1][r] = m

def naturalSelection(brood, broodFitness):
    probs = []
    for b in brood:
        if gk and b[0] == 28:  # like Genghis Khan
            s = 1
        else:
            s = b[0]/broodFitness
        probs.append(s)
    return random.choices(population=brood, weights=probs, k=2)
        
class Population(object):
    """population of board games with 8 queens randomly placed in each column"""
    def __init__(self, popSize, numIts, mutPct):
        self.broodFitness = 0
        self.brood = []
        self.performanceHistory = []
        self.familyTree = []
        if (v): print('creating brood')
        for i in range(0,popSize):
            newSpec = [0,[0,1,2,3,4,5,6,7]]
            # newSpec = [0,[0,0,0,0,0,0,0,0]]
            random.shuffle(newSpec[1])
            newSpec[0] = fitness(newSpec[1],0)
            self.broodFitness += newSpec[0]
            self.brood.append(newSpec)
        self.performanceHistory.append((self.broodFitness/popSize))
        self.familyTree.append([0,self.brood])
        self.trial(numIts, popSize, mutPct)
        
    def trial (self, numIts, popSize, mutPct):
        if (v): print('running stork experiments')
        solved = 0
        generations = 1
        for gen in range(1,numIts+1):
            if (v): print('generation',gen,sep='',end=' ')
            self.brood, self.broodFitness, solved = self.callTheStork(popSize, mutPct)
            if (solved): break
            self.performanceHistory.append((self.broodFitness/popSize))
            self.familyTree.append([generations,self.brood])
            generations += 1
        if (v): print('\n\nprinting final brood')
        self.printAndDestroyBrood()
        if (v):
            with open('familyTree.txt','w') as outFile:
                outFile.write('\nprinting entire family tree\n')
                for x in range(generations):
                    outFile.write(str(self.familyTree[x]))
                    outFile.write('\n')
        if (v):
            print('\nprinting peformance history')
            for g in range(generations):
                print('generation',g,'- average fitness',self.performanceHistory[g])
        if (v): print('\ngenerating performance history plot')
        self.plotResults(generations)
        
    def callTheStork(self, popSize, mutPct):
        """https://youtu.be/qScWb1HearI"""
        newBrood = []
        newBroodFitness = 0
        for i in range(int(popSize/2)):
            specA, specB = naturalSelection(self.brood, self.broodFitness)
            specC, specD = crossoverSpecimens(specA, specB)
            mutateSpecimen(specC, mutPct)
            mutateSpecimen(specD, mutPct)
            specC[0] = fitness(specC[1],0)
            specD[0] = fitness(specD[1],0)                
            newBroodFitness += specC[0]
            newBroodFitness += specD[0]
            newBrood.append(specC)
            newBrood.append(specD)
            if solutionHalt and (specC[0]==28 or specD[0]==28):
                if (v):
                    print('\n\nsolution found, spray them with a garden hose!')
                    printBoard(specC) if (specC[0] > specD[0]) else printBoard(specD)
                return newBrood, newBroodFitness, 1
        return newBrood, newBroodFitness, 0

    def printAndDestroyBrood(self):
        count = 0
        self.brood.sort(key=lambda item:item[0])
        while(self.brood and count < 1):
            count+=1
            print(count,": ",end='')
            printBoard(self.brood.pop())

    def plotResults(self, gens):
        plt.plot(range(0,gens),self.performanceHistory,'go-')
        plt.title('Genetic Algorithmic Solution to 8-Queens\nPerformance History')
        plt.xlabel('Generations')
        plt.ylabel('Average Fitness')
        plt.show()
        # plt.savefig('performanceHistory.png')

if __name__ == '__main__':
    timeStart = time.time()
    populationSize = int(input("enter the size of the inital population:  "))
    numIterations = int(input("enter the number of generations for the program to run:  "))
    mutationPct = int(input("enter the percentage likeleyhood, in integers, of mutation (0 is none and 100 is Teenage Mutantant Ninja Turtles Ooze):  "))/100
    gk = bool(input("enter True to trigger the super-breeder/Ghengis Khan setting, solutions breed with everyone, otherwise leave blank:  "))
    solutionHalt = bool(input("enter True to tell the program to halt as soon as a solution is found, otherwise leave blank:  "))  #toggle to halt the program when a solution is found, or allow the trial to complete the number of generations
    v = bool(input("enter True to trigger verbose reporting, otherwise leave blank:  "))

    if(v): print(f'\nPopulation Size: {populationSize}\nGenerations: {populationSize}\nMutation Percentage: {mutationPct*100}%\nSuper-Breeder / Ghengis Khan Toggle: {gk}\nHalt at Solution: {solutionHalt}\nVerbose Printing: {v}\nworking...')
    experiment = Population(populationSize,numIterations,mutationPct)
    if(v): print('... done working')

    timeEnd = time.time()
    timeRun = timeEnd - timeStart
    print('total program run time is',timeRun,'seconds.')
