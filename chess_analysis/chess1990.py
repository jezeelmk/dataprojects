import pandas as pd


url = "https://ratings.fide.com/toparc.phtml?cod=1"


df = pd.read_html(url)
print(df[4])

df[4].to_csv("chess200.csv")