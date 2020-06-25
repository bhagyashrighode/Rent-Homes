

import pandas as pd
import numpy as np
import sklearn.preprocessing
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
df=pd.read_csv("Pune.csv")

#Independent and depedent variable
X=df.iloc[:,1:4].values
X=pd.get_dummies(data=df.drop(['Area','Date','Sosciety'],axis=1),columns=['Type','BHK'])
y=df.iloc[:,0].values
#y=pd.get_dummies(y)

#Train-Test-Split data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)

#Standard Scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.fit_transform(X_test)

#KNN Algorithm
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=10)
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
print y_pred,y_test

from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
print accuracy_score(y_test,y_pred)*100
print confusion_matrix(y_test,y_pred)


#SVM Algorithm
from sklearn.svm import SVC
classifier=SVC(kernel='linear',random_state=0)
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
print accuracy_score(y_test,y_pred)*100

