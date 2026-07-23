from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder

income = ['High', 'High', 'Medium', 'Medium', 'Low',
          'Low', 'High', 'Medium', 'High', 'Low']

credit_score = ['Good', 'Good', 'Good', 'Average', 'Poor',
                'Average', 'Average', 'Good', 'Good', 'Poor']

employment = ['Permanent', 'Permanent', 'Permanent', 'Permanent', 'Temporary',
              'Temporary', 'Permanent', 'Temporary', 'Permanent', 'Temporary']

property = ['Yes', 'No', 'Yes', 'No', 'No',
            'Yes', 'Yes', 'No', 'Yes', 'Yes']

loan = ['Yes', 'Yes', 'Yes', 'Yes', 'No',
        'No', 'Yes', 'No', 'Yes', 'No']


le = LabelEncoder()
income = le.fit_transform(income)
credit_score = le.fit_transform(credit_score)
employment = le.fit_transform(employment)
property = le.fit_transform(property)
loan = le.fit_transform(loan)


X = list(zip(income, credit_score, employment, property))
y = loan


ann = MLPClassifier(hidden_layer_sizes=(2,), max_iter=5000)
ann.fit(X, y)

# Predict
# High, Good, Permanent, Yes
print("Prediction:", ann.predict([[0, 1, 0, 1]]))
