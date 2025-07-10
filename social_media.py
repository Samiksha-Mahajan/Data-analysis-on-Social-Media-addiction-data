import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('social_media.csv')
print(df)
print("*******************************************************")

#Display the first few rows of the dataset:
print(df.head())
print("*******************************************************")

#Get a summary of the dataset
print(df.info())
print("*******************************************************")
print(df.describe())
print("*******************************************************")

Total_stud_addicted = df['Student_ID'].count()
print("Total Student Addicted By Social Media = " ,Total_stud_addicted)

print(df.groupby('Gender')['Student_ID'].count())


print("*******************************************************")

print("Academic Levels Are : " , df['Academic_Level'].unique())
print("Mostly used Platform by students : " , df['Most_Used_Platform'].unique())

print("*******************************************************")

print("Count by Relationship status : ", df.groupby('Relationship_Status')['Gender'].count())


print("*******************************************************")
#Average daily hours used by Students by Gender

xpoint = df['Gender']
ypoint = df['Avg_Daily_Usage_Hours']
plt.title('Daily hour used by Gender')
plt.xlabel('Gender')
plt.ylabel('Daily Hours')
plt.bar(xpoint, ypoint, )
plt.show()

#Platform Affected Academic Performance or not

plt.figure(figsize = (8, 6))
x = df['Affects_Academic_Performance']

y = df['Most_Used_Platform']

plt.scatter(x , y, color = 'red')
plt.title('Platform Affect Academic Perfomance')
plt.xlabel('Academic perfomance')
plt.ylabel('Platform')
plt.show()































