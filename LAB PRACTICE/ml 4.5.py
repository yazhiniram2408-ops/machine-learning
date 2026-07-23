from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder

experience = ['High', 'High', 'Medium', 'Medium', 'Low',
              'High', 'Medium', 'Low', 'High', 'Low']

performance = ['Excellent', 'Good', 'Good', 'Average', 'Poor',
               'Excellent', 'Good', 'Average', 'Good', 'Poor']

leadership = ['Yes', 'Yes', 'Yes', 'No', 'No',
              'Yes', 'No', 'No', 'Yes', 'No']

training = ['Yes', 'Yes', 'Yes', 'Yes', 'No',
            'No', 'Yes', 'No', 'Yes', 'Yes']

promotion = ['Promoted', 'Promoted', 'Promoted', 'Not Promoted', 'Not Promoted',
             'Promoted', 'Promoted', 'Not Promoted', 'Promoted', 'Not Promoted']

le = LabelEncoder()
experience = le.fit_transform(experience)
performance = le.fit_transform(performance)
leadership = le.fit_transform(leadership)
training = le.fit_transform(training)
promotion = le.fit_transform(promotion)

X = list(zip(experience, performance, leadership, training))
y = promotion

ann = MLPClassifier(hidden_layer_sizes=(2,), max_iter=5000)
ann.fit(X, y)

# Predict
# High, Excellent, Yes, Yes
print("Prediction:", ann.predict([[0, 1, 1, 1]]))
