from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder

fever = ['Yes', 'Yes', 'No', 'Yes', 'No',
         'Yes', 'No', 'Yes', 'Yes', 'No']

cough = ['Yes', 'Yes', 'Yes', 'No', 'No',
         'Yes', 'Yes', 'No', 'Yes', 'No']

headache = ['Yes', 'No', 'Yes', 'Yes', 'No',
            'Yes', 'No', 'No', 'Yes', 'Yes']

body_pain = ['Yes', 'Yes', 'No', 'Yes', 'No',
             'No', 'Yes', 'Yes', 'Yes', 'No']

fatigue = ['Yes', 'Yes', 'No', 'Yes', 'No',
           'Yes', 'No', 'Yes', 'Yes', 'No']

disease = ['Positive', 'Positive', 'Negative', 'Positive', 'Negative',
           'Positive', 'Negative', 'Positive', 'Positive', 'Negative']

le = LabelEncoder()
fever = le.fit_transform(fever)
cough = le.fit_transform(cough)
headache = le.fit_transform(headache)
body_pain = le.fit_transform(body_pain)
fatigue = le.fit_transform(fatigue)
disease = le.fit_transform(disease)


X = list(zip(fever, cough, headache, body_pain, fatigue))
y = disease


ann = MLPClassifier(hidden_layer_sizes=(2,), max_iter=5000)
ann.fit(X, y)

# Predict
# Fever=Yes, Cough=Yes, Headache=Yes, Body Pain=Yes, Fatigue=Yes
print("Prediction:", ann.predict([[1, 1, 1, 1, 1]]))
