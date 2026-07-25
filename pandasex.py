import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C']);

# Define the path to our data file
path_1 = "./data/mexico-real-estate-1.csv"

# Print it to verify
print(f'We will load data from: "{path_1}"')


# Load the dataset using the variable we defined
(
 xtab := pd.read_csv(path_1)
)
xtab
print(xtab)


(
 pd.read_csv(path_1)
.head()
# .dropna()
 .info()
)