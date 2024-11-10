import pandas as pd

# Load the dataset
data = pd.read_csv('/Users/aami/Documents/assignment_aswathy/data/clean/wfh_tidy_person_p.csv')

# Display first 5 rows of the dataset
print(data.head())

# data quality and errors
print(data.isnull().sum())

print(data.dtypes)

data= data.dropna()

#binary data loaded as float convert to int as it is n=binary data and integer type is more appropriate than float

data['male'] = data['male'].astype(int)
print (data['male'])

# data filtering,creating new variable,transformation

# fliter treatment group 
treatment_data = data[data['treatment']==1]
print(treatment_data.head())

#creating new variable- taking the average of performance before and after the treatment. 
# perform10 is before and perform11 is after

data['avg_performance']= (data['perform10']+ data['perform11'])/2
print (data[['perform10','perform11','avg_performance']].head())

#Transformed data

data.to_csv('/Users/aami/Documents/assignment_aswathy/data/clean/processed_data.csv', index=False)

print('transformed data saved to processed_data.csv')

#summary statistics 

print(data.describe())
treatment_stats = data.groupby('treatment')['avg_performance'].mean()
print(treatment_stats)

## Visualisation of average performance
import matplotlib.pyplot as plt

# Plot histogram of average performance
data['avg_performance'].hist(bins=30)
plt.title('Average Performance Distribution')
plt.xlabel('Average Performance')
plt.ylabel('Frequency')
plt.show()

plt.savefig('/Users/aami/Documents/assignment_aswathy/graphs/average_performance_histogram.png')