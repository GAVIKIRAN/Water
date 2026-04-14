from sklearn.ensemble import RandomForestClassifier
import pickle

# sample dataset
X = [
 [7,5,300,200,25],
 [6.8,4,250,180,24],
 [9,10,500,400,30],
 [5,15,700,500,35]
]
y = [1,1,0,0]  # 1=Safe, 0=Unsafe

model = RandomForestClassifier()
model.fit(X,y)

pickle.dump(model, open("model.pkl","wb"))
print("Model saved!")