import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import re
import pandas as pd

x = [165, 15, 5, 2, 200]
c = [3000, 200, -50, 5000, 100]  # coefficient values

prediction = c[0] * x[0] + c[1] * x[1] + c[2] * x[2] + c[3] * x[3] + c[4] * x[4]

print(prediction)

a = 0.5
b = 3.2
x = 0
y = a + b * x
print(y)
x = 2
y = a + b * x
print(y)

# 18.9 3.8 7.4

# Python code to find Euclidean distance
# using linalg.norm()


#
# Humpty Dumpty sat on a wall,
# Humpty Dumpty had a great fall.
# All the king's horses and all the king's men
# Couldn't put Humpty together again.
dataset = [
    "Humpty Dumpty sat on a wall,",
    "Humpty Dumpty had a great fall.",
    "All the king's horses and all the king's me",
    "Couldn't put Humpty together again."
]
tfIdfVectorizer = TfidfVectorizer(use_idf=True)
tfIdf = tfIdfVectorizer.fit_transform(dataset)
df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)
print(df.head(25))

# intializing points in
# numpy arrays
point1 = np.array((14, 3, 0.8))
point2 = np.array((2, 6, 0.8))

# calculating Euclidean distance
dist = np.linalg.norm(point1 - point2)

print(dist)
