from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder


contains_link = ['Yes', 'Yes', 'No', 'Yes', 'No',
                 'Yes', 'Yes', 'No', 'Yes', 'No']

offer_words = ['Yes', 'Yes', 'No', 'No', 'Yes',
               'Yes', 'No', 'No', 'Yes', 'No']

unknown_sender = ['Yes', 'Yes', 'No', 'Yes', 'No',
                  'Yes', 'Yes', 'Yes', 'No', 'No']

attachment = ['No', 'Yes', 'No', 'No', 'Yes',
              'No', 'Yes', 'No', 'No', 'Yes']

many_recipients = ['Yes', 'Yes', 'No', 'Yes', 'No',
                   'No', 'Yes', 'No', 'Yes', 'No']

spam = ['Spam', 'Spam', 'Not Spam', 'Spam', 'Not Spam',
        'Spam', 'Spam', 'Not Spam', 'Spam', 'Not Spam']


le = LabelEncoder()
contains_link = le.fit_transform(contains_link)
offer_words = le.fit_transform(offer_words)
unknown_sender = le.fit_transform(unknown_sender)
attachment = le.fit_transform(attachment)
many_recipients = le.fit_transform(many_recipients)
spam = le.fit_transform(spam)


X = list(zip(contains_link, offer_words, unknown_sender,
             attachment, many_recipients))
y = spam


ann = MLPClassifier(hidden_layer_sizes=(2,), max_iter=5000)
ann.fit(X, y)

# Predict
# Contains Link=Yes, Offer Words=Yes, Unknown Sender=Yes,
# Attachment=No, Many Recipients=Yes
print("Prediction:", ann.predict([[1, 1, 1, 0, 1]]))
