from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# student study hours
x = [[1],[2],[3],[4],[5],[6],[7],[8]]
# results 
y = ["Fail", "Fail", "Fail", "Fail", "pass", "pass", "pass", "pass",]
# Ai model
model = DecisionTreeClassifier()
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25, random_state=42)
# Ai training 
model.fit(x_train,y_train)
hours = int(input( "How many hours student can do study?" ))
# prediction
prediction = model.predict([[hours]])
print("prediction:", prediction[0])
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
print("accuracy", accuracy*100,"%")