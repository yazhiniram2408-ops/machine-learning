from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

outlook = ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast',
           'Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain']

temperature = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool',
               'Mild','Cool','Mild','Mild','Mild','Hot','Mild']

humidity = ['High','High','High','High','Normal','Normal','Normal',
            'High','Normal','Normal','Normal','High','Normal','High']

wind = ['Weak','Strong','Weak','Weak','Weak','Strong','Strong',
        'Weak','Weak','Weak','Strong','Strong','Weak','Strong']

play = ['No','No','Yes','Yes','Yes','No','Yes',
        'No','Yes','Yes','Yes','Yes','Yes','No']


le = LabelEncoder()

outlook = le.fit_transform(outlook)
temperature = le.fit_transform(temperature)
humidity = le.fit_transform(humidity)
wind = le.fit_transform(wind)
play = le.fit_transform(play)


X = list(zip(outlook, temperature, humidity, wind))
y = play

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)


test = [[2, 0, 0, 0]]

prediction = clf.predict(test)

if prediction[0] == 1:
    print("Yes")
else:
    print("No")
