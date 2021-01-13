import pandas as pd                                           #importing python libraries like pandas and numpy
import numpy as np                                    
a=pd.read_csv('C:/Users/Admin/Desktop/heart dv.csv')                    #reading the CSV file

#prints entire data present in csv file
print(a)

#prints the number of records present in the file
print(len(a))

#the column names are printed
print(a.columns)

#information about the file is printed like no of enteries, rows , columns, etc.,
print(a.info())

#if any null values are present in the file
print(a.isnull())

#the shape(no of rows and columns)is printed
print(a.shape)

#the first five records are printed
print(a.head())

#the first ten records are printed
print(a.head(10))

#the last five records are printed
print(a.tail())

#the last ten records are printed
print(a.tail(10))

#the numerical operations like mean, median, max are performed
print(a.describe())

#the datatype is done like whether the data is integer, string or float
print(a.dtypes)

#counts and classifies all the record data

#for age column
print(a['age'].value_counts())

#for sex column
print(a['sex'].value_counts())

#for cp column
print(a['cp'].value_counts())

#for trestbps column
print(a['trestbps'].value_counts())

#for chol column
print(a['chol'].value_counts())

#for fbs column
print(a['fbs'].value_counts())

#for thalach column
print(a['thalach'].value_counts())

#for oldpeak column
print(a['oldpeak'].value_counts())

#the column sex data are grouped and from that aggregate of all the other columns are found out

#the minimum wrt sex column and other column
print(a.groupby('sex').agg(['min']))

#the maximum wrt sex column and other column
print(a.groupby('sex').agg(['max']))

#the mean wrt sex column and other column
print(a.groupby('sex').agg(['mean']))

#the median wrt sex column and other column
print(a.groupby('sex').agg(['median']))

#the numerical operations

#mean
print(a['trestbps'].mean())

#maximum
print(a['trestbps'].max())

#minimum
print(a['trestbps'].min())

#count
print(a['trestbps'].count())

#standard deviation
print(a['trestbps'].std())

#unique values
print(a['trestbps'].unique())
print(a['trestbps'].nunique())

#mathematical operations

#all the data in trestbps is multiplied by 2
print(a['trestbps']*2)

#all the data in trestbps is added by 2
print(a['oldpeak']+2)

#null values
print(a.isnull().sum())

#renaming the column target to Target
a.rename(columns={'target':'Target'},inplace=True)
#the changed name is printed
print(a.columns)

#in location of the age column the first five data is printed 
print(a.loc[:5,"age"])

#the data in age is grouped with other columns and the sum is found 
sum1= a.groupby(['age']).sum()
print('Sum of values, grouped by the age: ' + str(sum1))
