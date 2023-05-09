'''
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from sklearn.model_selection import train_test_split

import json
from pathlib import Path
from classes import Order, Truck
from gui import create_structures, create_orders, create_trucks

# data creating
structures_lst = create_structures()
order_lst = create_orders(structures_lst)
truck_list = create_trucks(structures_lst)

def preprocess_data(graph, algorithm_data, order_lst, structures_lst, truck_list):
    # Process the data and create features and labels
    # ...
    # Normalize the data
    # ...
    return {'features': normalized_features, 'labels': labels}


# Normalize the data
normalized_data = preprocess_data(graph, algorithm_data, order_lst, structures_lst, truck_list)

X_train, X_val, y_train, y_val = train_test_split(normalized_data['features'], normalized_data['labels'], test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_absolute_error'])

history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_val, y_val))

model.evaluate(X_val, y_val)
'''