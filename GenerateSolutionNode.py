import os
import time
import csv

results = []

for i in range(1, 50):
	print("Iteration: " + str(i))
	os.system("python GenerateDataSets.py " + str(i * 10))
	actualTime = time.time()
	os.system("python GenerateSolution.py")

	diffTime = (time.time()) - actualTime

	file = open("tmp.txt", 'r')
	cost = file.readline()
	file.close()
	os.remove("tmp.txt")
	
	results.append({'Nombre de villes': i * 10, 'Duration (s)': "{:.{}f}".format(diffTime, 2), 'Cout': cost})


if os.path.exists('solution.csv'):
	os.remove('solution.csv')
with open('solution.csv', 'wb') as csvfile:
	fieldnames = ['Nombre de villes', 'Duration (s)']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

	writer.writeheader()

	for result in results:
		writer.writerow(result)