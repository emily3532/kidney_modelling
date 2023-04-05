import math
import statistics
def classify_nb(training_filename, testing_filename):
    f1 = open(training_filename, "r")
    t1 = f1.readlines()
    train = []
    for l in t1:
      l = l.split(',')
      train.append(l)
    f2 = open(testing_filename, "r")
    t2 = f2.readlines()
    test = []
    for p in t2:
      p = p.split(',')
      test.append(p)
    
    yes, no = classify(train)
    
    y_summary = summary(yes)
    n_summary = summary(no)
    
    len_yes = len(yes)
    len_no = len(no)
    len_train = len(train)
    p_yes = len_yes/len_train
    p_no = len_no/len_train

    predictions = []
    for test_row in test:
      predictions.append(predict(y_summary, n_summary, test_row, p_yes, p_no))
    return predictions

def predict(y, n, row, p_yes, p_no):
                         
    for k in range(0, len(row)):
      mean, std, l = y[k]
      y_pdf = pdf(float(row[k]), mean, std)
      mean, std, l = n[k]
      n_pdf = pdf(float(row[k]), mean, std)
      p_yes*= y_pdf
      p_no*= n_pdf
    if p_no > p_yes:
       return "no"
    else:
       return "yes"
     
    
    
def pdf(x, mean, std):
    return (1/(std * math.sqrt(2 * math.pi))) * math.exp((-math.pow(float(x) - mean, 2))/(2 * math.pow(std, 2)))
                         
def classify(training):
  y = []
  n = []
  for i in range(0, len(training)):
    clas = training[i][-1].strip()
    if clas == "yes":
      y.append(training[i])
    else:
      n.append(training[i])
  return y, n

def summary(data):
  summary = []
  for k in data:
    del k[-1]
  for col in zip(*data):
    n = []
    for i in col:
      n.append(float(i))
    summary.append([mean(n), statistics.stdev(n), len(n)])
  return summary
   

def mean(data):
      return sum(data)/len(data)
  
#print(classify_nb('train.txt', 'test.txt'))