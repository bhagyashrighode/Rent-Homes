
import pandas as pd
import numpy as np
import sklearn.preprocessing
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
df=pd.read_csv("Pune.csv")

#Independent and depedent variable
X=df.iloc[:,2].values
X=pd.get_dummies(data=df.drop(['Area','Date','Sosciety'],axis=1),columns=['Type','BHK'])
y=df.iloc[:,0].values
#y=pd.get_dummies(y)

#Train-Test-Split data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)

##Standard Scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.fit_transform(X_test)

#LogisticRegression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=150,random_state=111)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
print accuracy_score(y_test,y_pred)*100


#DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
print y_pred,y_test
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
print accuracy_score(y_test,y_pred)*100



#GNB
from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB() 
gnb.fit(X_train, y_train) 
# making predictions on the testing set 
y_pred = gnb.predict(X_test)  
# comparing actual response values (y_test) with predicted response values (y_pred) 
from sklearn import metrics 
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)


#RandomForest Algorith
from sklearn.ensemble import RandomForestClassifier

cls=RandomForestClassifier(n_estimators=1000)

cls.fit(X_train,y_train)

y_pred=cls.predict(X_test)

print accuracy_score(y_test,y_pred)*100
