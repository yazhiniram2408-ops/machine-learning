from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder

cgpa = [9, 8, 7, 6, 5, 9, 8, 6, 7, 5]
communication = ['Excellent', 'Good', 'Good', 'Average', 'Poor',
                 'Excellent', 'Good', 'Average', 'Excellent', 'Poor']
internship = ['Yes', 'Yes', 'Yes', 'No', 'No',
              'Yes', 'No', 'Yes', 'Yes', 'No']
programming = ['Excellent', 'Good', 'Average', 'Average', 'Poor',
               'Good', 'Good', 'Average', 'Good', 'Average']
placement = ['Placed', 'Placed', 'Placed', 'Not Placed', 'Not Placed',
             'Placed', 'Placed', 'Not Placed', 'Placed', 'Not Placed']

le = LabelEncoder()
communication = le.fit_transform(communication)
internship = le.fit_transform(internship)
programming = le.fit_transform(programming)
placement = le.fit_transform(placement)

X = list(zip(cgpa, communication, internship, programming))
y = placement


ann = MLPClassifier(hidden_layer_sizes=(2,), max_iter=5000)
ann.fit(X, y)

# Predict
# CGPA=9, Communication=Excellent, Internship=Yes, Programming=Excellent
print("Prediction:", ann.predict([[9, 1, 1, 1]]))
