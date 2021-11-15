import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("studentlevel.csv")


student_df=df.loc[df['student_id']=='TRL_zny']
print(student_df.groupby("level")["attempt"].mean())

fig = px.scatter(df,x="level",y="attempt".mean())




fig.show()