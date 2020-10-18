import random
from tqdm import tqdm
from Path import Path,n,start, graph

psize = 100

population = []

for i in range(psize):
    population.append(Path())

generations = 1
limit = 1000
bestScore = 10000000000
bestPath = list(range(1,n))
pbar = tqdm(total=limit)
# pbar.update(1)
while generations <= limit:

    parents = population[:]
    matingPool = []

    max_fitness = max(parents, key=lambda x : x.fitness)
    min_fitness = min(parents, key=lambda x : x.fitness)
    th = (max_fitness.fitness + min_fitness.fitness) // 2
    parents.sort(key=lambda x:(1/x.fitness))
    totalFitness = sum((1/x.fitness) for x in parents)
    cumilative = 0
    cumilativeList = []
    for i in parents:
        cumilative += (1/i.fitness)
        cumilativeList.append(cumilative/totalFitness)
    # cumilativeList = cumilativeList
    # print(cumilativeList)
    
    # print(parents[0].fitness)
    #
    # for i in range(len(parents)):
    #     if parents[i].fitness <= th:
    #         matingPool.append(parents[i])

    # matingPool = parents[:]
    # print("Mating Pool Size: ", len(matingPool))

    population = []

    while len(population) < psize:
        x = random.random()
        y = random.random()
        i = 0
        done = 0
        while i < len(cumilativeList) and done == 0:
            if x < cumilativeList[i]:
                done = 1
            else:
                i += 1
        j = 0
        done = 0
        while j < len(cumilativeList) and done == 0:
            if y < cumilativeList[j]:
                done = 1
            else:
                j += 1
        # print(x.path)
        # print(y.path)
        # if i != j:
        #     if random.random() < 0.5:
        #         child = matingPool[x].crossover2(matingPool[y])
        #     else:
        #         child = matingPool[x].crossover2(matingPool[y])
        #     child.mutate()
        #
        #     population.append(child)
        if i != j:

            child1 = parents[i].crossover2(parents[j])
            child2 = parents[j].crossover2(parents[i])
            child1.mutate()
            child2.mutate()

            population.append(child1)
            population.append(child2)
    # print("Population Size: ", len(population))

    for i in population:
        if i.getFitness() < bestScore:
            bestScore = i.fitness
            bestPath = i.path
            # print("---------------Updated---------------")
            # print("Generation: ",generations, "Score:", bestScore);
            s = "Generation: " + str(generations) + " Score: " + str(bestScore)
            pbar.set_description(s)

    pbar.update(1)
    # pbar.set_description("Generation: ",generations, "Score:", bestScore)
    generations += 1

print()
print("BestScore: ", bestScore)
route = str(start) + ' -> ' + ' -> '.join(str(x) for x in bestPath) + ' -> ' + str(start)
print("BestPath: ", route)

