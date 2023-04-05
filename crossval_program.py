#This creates the file for cross validation data
def cross_val_file(data):
    with open(data, 'r') as datafile:
        f = datafile.readlines()
    folds = []
    y_values = []
    n_values = []
    for i in range(0,len(f)):
        if f[i].split(",")[-1].strip() == "yes":
            y_values.append(f[i])
        else:
            n_values.append(f[i])
    
    with open('pima_folds.csv', 'w') as foldfile:
        for k in range(1,9):
            st = "fold" + str(k) +"\n"
            for j in range(0,27):
                st+=y_values[j+(k-1)*27]
            for l in range(0,50):
                st+=n_values[l+(k-1)*50]
            foldfile.write(st)
        for k in range(9,11):
            st = "fold" + str(k) +"\n"
            for j in range(0,26):
                st+=y_values[j+(k-1)*26]
            for l in range(0,50):
                st+=n_values[l+(k-1)*50]
            foldfile.write(st)
  
cross_val_file("pima.csv")

#This performs cross validation, either using KNN or NB #algorithms previously written.
def cross_val(data, algo, *k):
    with open(data, 'r') as datafile:
        f = datafile.readlines()
    folds = []
    y_values = []
    n_values = []
    for i in range(0,len(f)):
        if f[i].split(",")[-1].strip() == "yes":
            y_values.append(f[i])
        else:
            n_values.append(f[i])

    for k in range(1,9):
        st = []
        for j in range(0,27):
            st.append(y_values[j+(k-1)*27])
        for l in range(0,50):
            st.append(n_values[l+(k-1)*50])
        folds.append(st)
    for k in range(9,11):
        st = []
        for j in range(0,26):
            st.append(y_values[j+(k-1)*26])
        for l in range(0,50):
            st.append(n_values[l+(k-1)*50])
        folds.append(st)
        
    accuracy_total = 0
    for f in range(0, len(folds)):
        
        test_fold = folds[f]


        test = []
        for p in test_fold:
          p = p.split(',')
          test.append(p)
            
        actual_ans = []
        formatted_test = []
        for t in range(0, len(test)):
            actual_ans.append(test[t][-1].strip())
            formatted_test.append(test[t][:-1])
        train_fold=[]
        for r in range(0, len(folds)):
            if r != f:
                for x in range(0, len(folds[r])):
                    train_fold.append(folds[r][x])
        train = []
        for l in train_fold:
            l = l.split(',')
            train.append(l)
        if algo == "NB":
            results = classify_nb(train, formatted_test)
        if algo == "NN":
            results = classify_nn(train, formatted_test, k)

        correct = 0
        for res in range(0, len(results)):
            if results[res] == actual_ans[res]:
                correct += 1
    
        accuracy_total += correct/len(actual_ans)
    return accuracy_total/10


# print(cross_val("pima.csv", "NN", 5))
#print(cross_val("pima.csv", "NB"))
#print(cross_val("pima_CFS.csv","NB"))
import time
start = time.time()
print(cross_val("pima.csv", "NN", 1))
end = time.time()
print(end-start)