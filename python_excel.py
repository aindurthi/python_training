import pandas as pd
xls = pd.ExcelFile('C:\\Users\\admin\\Google Drive\\acharya\\python\\Copy_Input.xls')
df = xls.parse('Volume')
for i in df.iterrows():
    for i in df.columns():
        print i

