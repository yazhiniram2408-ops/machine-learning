from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

cgpa = ['High', 'High', 'Medium', 'Medium', 'Low',
        'High', 'Low', 'Medium', 'High', 'Low']

communication = ['Good', 'Excellent', 'Good', 'Average', 'Poor',
                 'Good', 'Average', 'Good', 'Excellent', 'Poor']

internship = ['Yes', 'Yes', 'Yes', 'No', 'No',
              'No', 'No', 'Yes', 'Yes', 'Yes']

programming = ['Good', 'Excellent', 'Good', 'Average', 'Poor',
               'Good', 'Average', 'Excellent', 'Good', 'Average']

placement = ['Yes', 'Yes', 'Yes', 'No', 'No',
             'Yes', 'No', 'Yes', 'Yes', 'No']


le = LabelEncoder()

cgpa = le.fit_transform(cgpa)
communication = le.fit_transform(communication)
internship = le.fit_transform(internship)
programming = le.fit_transform(programming)
placement = le.fit_transform(placement)

X = list(zip(cgpa, communication, internship, programming))
y = placement

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)


test = [[0, 2, 1, 2]]

prediction = clf.predict(test)

if prediction[0] == 1:
    print("Yes")
else:
    print("No")
