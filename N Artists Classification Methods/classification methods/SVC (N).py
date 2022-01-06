import pandas as pd
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import collections

tfidf = pd.read_csv(f'../tfidf_data/global_tfidf').drop(['Unnamed: 0','index'],axis=1)

print('------------------------------------------------')
n_rep = int(input('Number of repetitions : '))


list_accuracy = []
for j in range(n_rep):
    tfidf = tfidf.sample(frac=1)

    if j%(n_rep/10) ==0 :
        print(f'{j}/{n_rep}')

    rows, columns = tfidf.shape
    b = columns - 1
    X_train = tfidf.iloc[:, :-1][:int(rows // (10 / 8))]
    X_test = tfidf.iloc[:, :-1][int(rows // (10 / 8)):]
    y_train = tfidf.iloc[:, b:][:int(rows // (10 / 8))]
    y_test = tfidf.iloc[:, b:][int(rows // (10 / 8)):]

    # Create Decision Tree classifer object
    svm = SVC(decision_function_shape = "ovr")

    # Train Decision Tree Classifer
    svm = svm.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = svm.predict(X_test)

    compteur = 0
    y_test_ = [y for y in y_test['Target']]
    for i in range(len(y_pred)):
        if y_pred[i] == y_test_[i]:
            # print('Bonne prédiction')
            compteur += 1
    list_accuracy.append(compteur / len(y_pred))


plt.scatter(pd.DataFrame.from_dict(dict(collections.Counter(list_accuracy)),orient='index').reset_index()['index'],
        pd.DataFrame.from_dict(dict(collections.Counter(list_accuracy)),orient='index').reset_index()[0])
plt.show()