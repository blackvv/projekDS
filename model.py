# Importing necessary libraries
import pandas as pd # To manage data as data frames
import numpy as np # To manipulate data as arrays
from sklearn.linear_model import LogisticRegression # Classification model
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Importing the dataset
data = pd.read_csv('./datakuisioner-c.csv')

# Dictionary containing the mapping
variety_mappings = {0: 'Normal Gamer', 1: 'Risky Gamer', 2: 'Disorder Gamer'}

# Encoding the target variables to integers
#data = data.replace(['Normal Gamer', 'Risky Gamer' , 'Disorder Gamer'], [0, 1, 2])

X = data[['Keasyikan', 'Toleransi', 'Penarikan', 'Kegigihan', 'Pelarian', 'Masalah', 'Penipuan', 'Pemindahan', 'Konflik']]
y = data['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7)

#logreg = LogisticRegression(max_iter=1000) # Initializing the Logistic Regression model
#logreg.fit(X, y) # Fitting the model
modelsvmLinear = SVC(
  kernel = 'linear',
  C = 1
)
modelsvmLinear.fit(X_train, y_train)

# Function for classification based on inputs
def classify(a, b, c, d, e, f, g, h, i):
    arr = np.array([a, b, c, d, e, f, g, h, i]) # Convert to numpy array
    arr = arr.astype(np.float64) # Change the data type to float
    query = arr.reshape(1, -1) # Reshape the array
    prediction = variety_mappings[modelsvmLinear.predict(query)[0]] # Retrieve from dictionary
    return prediction # Return the prediction
