import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tnt_board as board


class specimen(object):
    def __init__(self,brdgme):
        self.spec = [0,[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]
        # random.shuffle(self.spec[1])
        # random.shuffle(self.spec[2])

        # make sure there are no illegal star placements in initial specimen
        if (0):
            viable = False
            while (viable == False):
                viable = True
                random.shuffle(self.spec[1])
                random.shuffle(self.spec[2])
                for i in range(0,9):
                    if (self.spec[1][i] == self.spec[2][i]):
                        viable = False
        
        self.fitness(brdgme, False)
        if (0 and v): print('New Specimen:',self.spec)
   
    def fitness(self, brdgme, printBool):
        v = False

        if (1):  # make sure there are no illegal star placements
            viable = False
            while (viable == False):
                viable = True
                random.shuffle(self.spec[1])
                random.shuffle(self.spec[2])
                for i in range(0,9):
                    if (self.spec[1][i] == self.spec[2][i]):
                        viable = False

        stars = self.makeStars()
        adjoiningStars = 0
        sadRegions = 0
        hapsburgFlag = False

        for i in range(0,9):
            if (self.spec[1][i] == self.spec[1][i+1]-1):
                adjoiningStars += 1
                if (v or printBool): print('group 1 & 1 - (',i,',',self.spec[1][i],') , (',i+1,',',self.spec[1][i+1],')')
            if (self.spec[1][i] == self.spec[1][i+1]  ): 
                adjoiningStars += 1
                if (v or printBool): print('group 1 & 1 - (',i,',',self.spec[1][i],') , (',i+1,',',self.spec[1][i+1],')')
            if (self.spec[1][i] == self.spec[1][i+1]+1): 
                adjoiningStars += 1
                if (v or printBool): print('group 1 & 1 - (',i,',',self.spec[1][i],') , (',i+1,',',self.spec[1][i+1],')')

            if (self.spec[2][i] == self.spec[2][i+1]-1):
                adjoiningStars += 1
                if (v or printBool): print('group 2 & 2 - (',i,',',self.spec[2][i],') , (',i+1,',',self.spec[2][i+1],')')
            if (self.spec[2][i] == self.spec[2][i+1]  ): 
                adjoiningStars += 1
                if (v or printBool): print('group 2 & 2 - (',i,',',self.spec[2][i],') , (',i+1,',',self.spec[2][i+1],')')
            if (self.spec[2][i] == self.spec[2][i+1]+1): 
                adjoiningStars += 1
                if (v or printBool): print('group 2 & 2 - (',i,',',self.spec[2][i],') , (',i+1,',',self.spec[2][i+1],')')

            if (self.spec[1][i] == self.spec[2][i]-1)  : 
                adjoiningStars += 1
                if (v or printBool): print('group 1 & 2 same row - (',i,',',self.spec[1][i],') , (',i,',',self.spec[2][i],')')
            if (self.spec[1][i] == self.spec[2][i]  )  : 
                adjoiningStars += 1
                # hapsburgFlag = True
                if (v or printBool): print('group 1 & 2 same row - (',i,',',self.spec[1][i],') , (',i,',',self.spec[2][i],') inbred')
            if (self.spec[1][i] == self.spec[2][i]+1)  : 
                adjoiningStars += 1
                if (v or printBool): print('group 1 & 2 same row - (',i,',',self.spec[1][i],') , (',i,',',self.spec[2][i],')')
            
            # if (self.spec[2][i] == self.spec[1][i]-1)  : 
            #     adjoiningStars += 1
            #     if (v or printBool): print('group 2 & 1 same row - (',i,',',self.spec[2][i],') , (',i,',',self.spec[1][i],')')
            # if (self.spec[2][i] == self.spec[1][i]  )  : 
            #     hapsburgFlag = True
            #     if (v or printBool): print('group 2 & 1 same row - (',i,',',self.spec[2][i],') , (',i,',',self.spec[1][i],')')
            # if (self.spec[2][i] == self.spec[1][i]+1)  : 
            #     adjoiningStars += 1
            #     if (v or printBool): print('group 2 & 1 same row - (',i,',',self.spec[2][i],') , (',i,',',self.spec[1][i],')')

            if (self.spec[1][i] == self.spec[2][i+1]-1): 
                adjoiningStars += 1 
                if (v or printBool): print('group 1 & 2 diff row - (',i,',',self.spec[1][i],') , (',i+1,',',self.spec[2][i+1],')')
            if (self.spec[1][i] == self.spec[2][i+1]  ): 
                adjoiningStars += 1
                if (v or printBool): print('group 1 & 2 diff row - (',i,',',self.spec[1][i],') , (',i+1,',',self.spec[2][i+1],')')
            if (self.spec[1][i] == self.spec[2][i+1]+1): 
                adjoiningStars += 1
                if (v or printBool): print('group 1 & 2 diff row - (',i,',',self.spec[1][i],') , (',i+1,',',self.spec[2][i+1],')')
        
            if (self.spec[2][i] == self.spec[1][i+1]-1): 
                adjoiningStars += 1 
                if (v or printBool): print('group 2 & 1 diff row - (',i,',',self.spec[2][i],') , (',i+1,',',self.spec[1][i+1],')')
            if (self.spec[2][i] == self.spec[1][i+1]  ): 
                adjoiningStars += 1
                if (v or printBool): print('group 2 & 1 diff row - (',i,',',self.spec[2][i],') , (',i+1,',',self.spec[1][i+1],')')
            if (self.spec[2][i] == self.spec[1][i+1]+1): 
                adjoiningStars += 1
                if (v or printBool): print('group 2 & 1 diff row - (',i,',',self.spec[2][i],') , (',i+1,',',self.spec[1][i+1],')')

        for region in brdgme.regionList:
            starCount = 0
            for star in stars:
                if star in region[1]:
                    starCount += 1
            if starCount < 2:
                sadRegions += 1
        
        if hapsburgFlag == True:
            fitnessScore = 0
        else:
            fitnessScore = maxFitness - adjoiningStars - sadRegions
        
        self.spec[0] = fitnessScore

        if (v or printBool):
            print('Specimen:',self.spec)
            print('Hapsburgian?',hapsburgFlag,' Adjoining Stars:',adjoiningStars,' Unsatisfied Regions:',sadRegions,' Fitness Score:',fitnessScore)
    
    def mutateSpecimen(self, mutPct):
        mutateBool = mutPct >= random.random()
        if (0 and v): 
            print('mutateBool:',mutateBool)
            print('specimen before mutation function:',self.spec)
        if (mutateBool):
            starBatch = random.randint(1,2)
            r = random.choices(population=(range(0,10)), k=2)
            temp = self.spec[starBatch][r[0]]
            self.spec[starBatch][r[0]] = self.spec[starBatch][r[1]]
            self.spec[starBatch][r[1]] = temp
            # r = random.randint(0,9)
            # m = random.randint(0,9)
            # self.spec[starBatch][r] = m
        if (0 and v):
            print('specimen after mutation function: ',self.spec)

    def makeStars(self):
        stars = []
        for row in range(10):
            starOne = (row,self.spec[1][row])
            starTwo = (row,self.spec[2][row])
            stars.append(starOne)
            stars.append(starTwo)
        return stars

    def printBoard(self,brdgme):
        self.fitness(brdgme, True)
        brdgme.print_board(self.makeStars())

        
class Population(object):
    """population of board arrangements with Stars randomly placed in each column"""
    def __init__(self, popSize, numIts, mutPct, brdgme, best):
        self.broodFitness = 0
        self.brood = []
        self.performanceHistory = []
        self.familyTree = []
        if (v): print('creating brood')
        for i in range(0,popSize):
            newSpec = specimen(brdgme)
            self.broodFitness += newSpec.spec[0]
            self.brood.append(newSpec)
            if (newSpec.spec[0] > best.spec[0]): best = newSpec
            if (v): print('specimen #',i,' - fitness score = ',newSpec.spec[0],sep='')
        self.performanceHistory.append((self.broodFitness/popSize))
        self.familyTree.append([0,self.brood])
        self.trial(numIts, popSize, mutPct, brdgme, best)
        
    def trial (self, numIts, popSize, mutPct, brdgme, best):
        if (v): print('running stork experiments')
        solved = 0
        generations = 1
        for gen in range(1,numIts+1):
            if (0 and v): print('\n\nGeneration',gen)
            self.brood, self.broodFitness, solved = self.callTheStork(popSize, mutPct, gen, brdgme, best)
            if (solved): break
            self.performanceHistory.append((self.broodFitness/popSize))
            self.familyTree.append([generations,self.brood])
            if (v): print('Generation',generations,'- Total Fitness =',self.broodFitness,'- Gen Avg Fitness =',self.broodFitness/popSize)
            generations += 1
        if (v): print('\n\nprinting final brood')
        self.printAndDestroyBrood(brdgme)
        if (1):
            print('Best Overall Specimen')
            best.printBoard(brdgme)
        if (v): 
            print('\nPerformance History:',self.performanceHistory)
            print('\ngenerating performance history plot')
        self.plotResults(generations)
        
    def callTheStork(self, popSize, mutPct, gen, brdgme, best):
        """https://youtu.be/qScWb1HearI"""
        newBrood = []
        newBroodFitness = 0
        for i in range(int(popSize/2)):
            specA, specB = self.naturalSelection()
            if (1): # and gen < 40):
                specC, specD = self.crossoverSpecimens(specA, specB)
            else:
                specC, specD = specA, specB
            specC.mutateSpecimen(mutPct)
            specD.mutateSpecimen(mutPct)
            specC.fitness(brdgme, False)
            specD.fitness(brdgme, False)                
            newBroodFitness += specC.spec[0]
            newBroodFitness += specD.spec[0]
            newBrood.append(specC)
            newBrood.append(specD)
            if specC.spec[0] > best.spec[0]: best = specC
            if specD.spec[0] > best.spec[0]: best = specD
            if solutionHalt and (specC.spec[0]==maxFitness or specD.spec[0]==maxFitness):
                if (v):
                    print('\n\nsolution found, spray them with a garden hose!')
                    specC.printBoard(brdgme) if (specC.spec[0] > specD.spec[0]) else specD.printBoard(brdgme)
                return newBrood, newBroodFitness, 1
        return newBrood, newBroodFitness, 0

    def naturalSelection(self):
        probs = []
        for b in self.brood:
            # if gk and b.spec[0] == maxFitness:  # like Genghis Khan
                # s = 1
            # elif b.spec[0] < 44:
            #     s = 0
            # else:
            #     s = pow(b.spec[0], emphasis)/self.broodFitness
            s = pow(b.spec[0], emphasis) #/self.broodFitness
            probs.append(s)
        if (0 and v): print('breeding probabilities:',probs)
        breeders = random.choices(population=self.brood, weights=probs, k=2)
        if (0 and v): print('breeding pair:\n',breeders[0].spec,'\n', breeders[1].spec)
        return breeders

    def crossoverSpecimens(self, specA, specB):
        # starBatch = random.randint(1,2)
        # r = random.randint(0,9)
        # temp = specA.spec[starBatch][0:r] + specB.spec[starBatch][r:10]
        # specB.spec[starBatch] = specB.spec[starBatch][0:r] + specA.spec[starBatch][r:10]
        # specA.spec[starBatch] = temp
       
        starBatch = random.randint(1,2)
        temp = specA.spec[starBatch]
        specA.spec[starBatch] = specB.spec[starBatch]
        specB.spec[starBatch] = specA.spec[starBatch]
       
        return specA, specB

    def printAndDestroyBrood(self, brdgme):
        count = 0
        self.brood.sort(key=lambda item:item.spec[0])
        while(self.brood and count < 1):
            count+=1
            print('Rank in Brood:',count)
            curSpec = self.brood.pop()
            curSpec.printBoard(brdgme)

    def plotResults(self, gens):
        
        # plot the actual fitness measurements
        plt.plot(range(0,gens),self.performanceHistory,'o-', alpha=0.3, label='Average Fitness Measurement')
        
        if (1):  # plot a moving average 
            data = {'periods':range(0,gens), 'scores':self.performanceHistory}
            data = pd.DataFrame(data)
            data['movingAverage'] = data.iloc[:,1].rolling(window=(int(gens/10))).mean()
            plt.plot(range(0,gens) ,data['movingAverage'], '-', label='Moving Average')
        
        if (0):  # plot a straight line average
            lineCalc = np.polyfit(range(0,gens), self.performanceHistory, 1)
            linePlot = np.poly1d(lineCalc)
            plt.plot(range(0,gens), linePlot(range(0,gens)), '-', label='Straight Line Average')
        
        # actual plot parameters
        plt.title('Genetic Algorithmic Solution to TwoNotTouch / StarBattle\nPerformance History')
        plt.xlabel('Generations')
        plt.ylabel('Average Fitness')
        plt.legend()
        plt.show()
        # plt.savefig('performanceHistory.png')

if __name__ == '__main__':
    timeStart = time.time()
    
    if (0):
        populationSize = int(input("enter the size of the inital population:  "))
        numIterations = int(input("enter the number of generations for the program to run:  "))
        mutationPct = int(input("enter the percentage likeleyhood, in integers, of mutation (0 is none and 100 is Teenage Mutantant Ninja Turtles Ooze):  "))/100
        maxFitness = 55 # total number of adjointing pairs of stars plus empty regions
        gk = bool(input("enter True to trigger the super-breeder/Ghengis Khan setting, solutions breed with everyone, otherwise leave blank:  "))
        solutionHalt = bool(input("enter True to tell the program to halt as soon as a solution is found, otherwise leave blank:  "))  #toggle to halt the program when a solution is found, or allow the trial to complete the number of generations
        v = bool(input("enter True to trigger verbose reporting, otherwise leave blank:  "))
    else:
        populationSize = 100
        numIterations = 1000000
        mutationPct = 0.50
        emphasis = 3
        maxFitness = 55 # total number of adjointing pairs of stars plus empty regions
        gk = True
        solutionHalt = True
        v = True
    
    if(v): print(f'\nPopulation Size: {populationSize}\nGenerations: {populationSize}\nMutation Percentage: {mutationPct*100}%\nMaximum Fitness Score: {maxFitness}\nSuper-Breeder / Ghengis Khan Toggle: {gk}\nHalt at Solution: {solutionHalt}\nVerbose Printing: {v}\nworking...')
    game = board.board(board.boardList.b)
    best = specimen(game)
    experiment = Population(populationSize,numIterations,mutationPct,game,best)
    if(v): print('... done working')

    timeEnd = time.time()
    timeRun = timeEnd - timeStart
    print('total program run time is',timeRun,'seconds.')
