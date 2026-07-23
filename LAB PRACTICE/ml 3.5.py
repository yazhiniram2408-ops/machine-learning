from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

fever = ['Yes', 'Yes', 'No', 'Yes', 'No',
         'Yes', 'No', 'Yes', 'Yes', 'No']

cough = ['Yes', 'Yes', 'Yes', 'No', 'No',
         'Yes', 'Yes', 'No', 'Yes', 'No']

headache = ['Yes', 'No', 'Yes', 'Yes', 'No',
            'Yes', 'No', 'No', 'Yes', 'Yes']

body_pain = ['Yes', 'Yes', 'No', 'Yes', 'No',
             'No', 'Yes', 'Yes', 'Yes', 'No']

disease = ['Positive', 'Positive', 'Negative', 'Positive', 'Negative',
           'Positive', 'Negative', 'Positive', 'Positive', 'Negative']

le = LabelEncoder()

fever = le.fit_transform(fever)
cough = le.fit_transform(cough)
headache = le.fit_transform(headache)
body_pain = le.fit_transform(body_pain)
disease = le.fit_transform(disease)

X = list(zip(fever, cough, headache, body_pain))
y = disease


clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)


test = [[1, 1, 1, 1]]

prediction = clf.predict(test)

if prediction[0] == 1:
    print("Positive")
else:
    print("Negative")
