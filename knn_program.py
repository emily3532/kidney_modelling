import math
def classify_nn(training_file, testing_file, k):
    predictions = []
    f1 = open(training_file, "r")
    t1 = f1.readlines()
    train = []
    for l in t1:
      l = l.split(',')
      train.append(l)
    f2 = open(testing_file, "r")
    t2 = f2.readlines()
    test = []
    for p in t2:
      p = p.split(',')
      test.append(p)

    for row in test:
      output = predict(train, row, k)
      predictions.append(output)
    return(predictions)
  
def eucld(row1, row2):
    dist = 0.0
    for i in range(len(row1)-1):
      dist += (float(row1[i]) - float(row2[i]))**2
    return math.sqrt(dist)
 
def neighs(train, test_row, num):
    distances = []
    for train_row in train:
      dist = eucld(train_row, test_row)
      distances.append((train_row, dist))
    #sorts the distance tuples by their distance
    distances.sort(key=lambda tup: tup[1])
    neighbors = []
    for i in range(num):
      neighbors.append(distances[i][0])
    return neighbors
  
def predict(train, test_row, num):
    neighbors = neighs(train, test_row, num)
    outputs = [row[-1] for row in neighbors]
    prediction = max(outputs, key=outputs.count)
    return prediction.strip()
 