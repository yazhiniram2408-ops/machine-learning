from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


income = ['High', 'High', 'Medium', 'Low', 'Medium',
          'High', 'Low', 'Medium', 'High', 'Low']

credit_score = ['Good', 'Good', 'Good', 'Poor', 'Average',
                'Average', 'Poor', 'Good', 'Good', 'Average']

employment = ['Permanent', 'Permanent', 'Permanent', 'Temporary', 'Permanent',
              'Temporary', 'Temporary', 'Permanent', 'Permanent', 'Temporary']

property = ['Yes', 'No', 'Yes', 'No', 'No',
            'Yes', 'Yes', 'Yes', 'Yes', 'No']

loan = ['Yes', 'Yes', 'Yes', 'No', 'Yes',
        'No', 'No', 'Yes', 'Yes', 'No']


le = LabelEncoder()

income = le.fit_transform(income)
credit_score = le.fit_transform(credit_score)
employment = le.fit_transform(employment)
property = le.fit_transform(property)
loan = le.fit_transform(loan)

X = list(zip(income, credit_score, employment, property))
y = loan


clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)


test = [[0, 2, 0, 1]]

prediction = clf.predict(test)

if prediction[0] == 1:
    print("Yes")
else:
    print("No")
