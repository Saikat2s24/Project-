import pandas

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier


dataset = pandas.read_csv('data.csv')

x = dataset["input"]
y = dataset["output"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=42)
vectorizer = TfidfVectorizer()
conversion = vectorizer.fit_transform(x_train)

model = RandomForestClassifier()
model.fit(conversion, y_train)
new_message = ["Congratulations! You've won a free ticket to Bahamas. Click here to claim your prize."]
n_conversion = vectorizer.transform(new_message)
prediction = model.predict(n_conversion)
print(prediction[0])