import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import collections

artist1 = input('1er artist sur lequel on souhaite effectuer le test : ')
artist2 = input('2ème artist sur lequel on souhaite effectuer le test : ')

tfidf = pd.read_csv(f'tfidf_data/tfidf_{artist1}_{artist2}')

list_accuracy = []
for j in range(1000):
    tfidf = tfidf.sample(frac=1)

    rows, columns = tfidf.shape
    b = columns - 1
    X_train = tfidf.iloc[:, :-1][:int(rows // (10 / 8))]
    X_test = tfidf.iloc[:, :-1][int(rows // (10 / 8)):]
    y_train = tfidf.iloc[:, b:][:int(rows // (10 / 8))]
    y_test = tfidf.iloc[:, b:][int(rows // (10 / 8)):]

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier()

    # Train Decision Tree Classifer
    clf = clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

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