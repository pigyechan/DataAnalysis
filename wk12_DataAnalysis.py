file1= pd.read_csv("c:\\python_work\\convience_1.csv")
file2= pd.read_csv("c:\\python_work\\convience_2.csv")
df=pd.concat([file1, file2])
df["급여"] = 0
df["급여"] = df["근무시간"]*df["시급"]
finalData = df.sort_values(by=['급여'], ascending = False)
finalData.to_csv("c:\\python_work\\2019101412_이예찬_test1.csv")