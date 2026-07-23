from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


experience = ['High', 'High', 'Medium', 'Low', 'Medium',
              'Low', 'High', 'Medium', 'High']

performance = ['Excellent', 'Good', 'Good', 'Average', 'Excellent',
               'Poor', 'Good', 'Average', 'Excellent']

leadership = ['Yes', 'Yes', 'No', 'No', 'Yes',
              'No', 'Yes', 'No', 'Yes']

training = ['Yes', 'Yes', 'Yes', 'No', 'Yes',
            'No', 'No', 'Yes', 'Yes']

promotion = ['Yes', 'Yes', 'Yes', 'No', 'Yes',
             'No', 'Yes', 'No', 'Yes']

le = LabelEncoder()

experience = le.fit_transform(experience)
performance = le.fit_transform(performance)
leadership = le.fit_transform(leadership)
training = le.fit_transform(training)
promotion = le.fit_transform(promotion)

X = list(zip(experience, performance, leadership, training))
y = promotion

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)


test = [[0, 1, 1, 1]]

prediction = clf.predict(test)

if prediction[0] == 1:
    print("Yes")
else:
    print("No")
