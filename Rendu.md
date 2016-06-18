#Labo MLG - Genetic Algorithms
##A tool for optimization

David Kunzmann and Toni Dias

HEIG-VD

19.06.2016

###6.1 - Problem (TPS)
The travelling salesman problem (TSP) asks the following question: Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city? It is an NP-hard problem in combinatorial optimization, important in operations research and theoretical computer science.
The objective of this exercise is to solve the TSP problem for a set of 14 cities in Burma, officially the Republic of the Union of Myanmar. The following vectors give the GPS position of each city.

####Our Solution
In our solution, we used haversine a pipy library. This lib helps us to calculate the distance between two GPS points.
Source: https://pypi.python.org/pypi/haversine

We initialize our genome with 14 random values in the range [0:13] (each value represents one GPS point).
We calculate the fitness value with the total distance of the travelling. If the chromosome contains all GPS points we keep a good fitness. But if the chromosome contains multiple GPS points and don't have all the points we put a big penalty.

###6.2 - Results
For all our results we used a seed of 123.
Our better travelling is the GPS points in this order with the link between the last and the first point.

	[10, 8, 9, 0, 1, 13, 2, 3, 4, 5, 11, 6, 12, 7]

the distance of the travel is 

	3354.52313748 km

###6.3 - Fitness function
For the fitness function, we decide calculate the total distance between points. This value is our fitness value. If all GPS points are on the chromosome (the travel pass in the all cities) we calculate the total distance. And return a big value (in our code 15000) and subtract the total distance. This method return a big number if the total distance is better.

But if the chromosome contains duplicate GPS points (and don't pass in the all cities) we put a penalty we calculate it like that:

	1 - (length of a chromosome - number of different values in the chromosome) * 0.05

The fitness is in the range ]0:1[. This is so big penalty and we wish the chromosome aren't selected for the next generations.

###6.4 - Explain the way you encoded the solution
####Chromosome example
A good chromosome, he has all cities: **[0,1,2,3,4,5,6,7,8,9,10,11,12,13]**

A bad chromosome, he hasn't all cities: **[0,1,2,0,4,5,6,7,8,9,0,11,12,13]**

###6.5 - Provide the configuration of the GA
To find our better solution, we used the parameters:

- mutation: 0.01 
 	- 0.01 because if we augment the mutation, we lose the good chromosome after the mutation. In example, we have a chromosome with all cities if it mutate, this chromosome isn't more a good chromosome.
- crossover: 0.9
- population size: 100 
	- after a lot of testes, we conclude with a population of 100 we have the same results so a bigger population. And in a better time.
- type of selection: GTournamentSelector
	- We choose this selector because after testes this is the best choice. We suppose the reason is when the first chromosome with a good fitness is funded, the algorithm take these parents and replace that. At the end, we have a minimum "local" result and this is not the best.
- number of generations: 250
	- when we make a testes with 500 generations, we see after about 220 generations the best fitness was founded. So we choose 250 to have a little marge. 


###6.6 - Plots, experimentations and explanations
100 Generations and 100 populations
The First (for reference)
![first fitness scores](IMG/Fitness_100_100_001_09.PNG =500x)
![first population generation](IMG/Pop_100_100_001_09.PNG =500x)

We can see in the first chart the range of fitness is very big. This is because we put a big penalty if the chromosome don't have all cities.
In the second chart, we see the first 20 generations don't have only one good chromosome this is because when we generate chromosomes we have a little chance to have a chromosome with 14 GPS points difference.

500 Generations and  500 populations
![500 fitness scores](IMG/Fitness_500.PNG =500x)
![500 population 500 generation](IMG/Pop_500.PNG =500x)

We can see the fitness score don't evolve a lot after 100 generations, the programme found the best solution and don't change there.
The same can observe in the second chart. After fund a good solution (a chromosome with 14 GPS points difference), the evolution don't change a lot after 100-120 generations.
###6.7 - Conclusion
We appreciate a lot work in this project. We can practice the theory view in courses and made a complete program with a result at the end. This is the best project of the semester and also the most interesting.

This course introduces us the machine learning programation and we are happy to have the chance to learn that. It's a discipline to grow up very fast and give us a good skill for our future CV. This project is a good example for us.