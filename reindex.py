import pandas as pd

SET = 2

df1 = pd.read_csv(f"kani_set{SET}.csv")
df2 = pd.read_csv(f"set_{SET}.csv")

df1["Bead_number"] = df1["Bead_number"].astype(str)
df2["Filename"] = df2["Filename"].astype(str)

df2["Bead_number"] = df2["Filename"].apply(
  lambda x: x
  .replace(".mp4", "")
  .split("b")[1]
)

df1 = df1.merge(df2, left_on="Bead_number", right_on="Bead_number", how="inner")
df2 = df2.drop(columns=["i", "Unnamed: 11"], errors='ignore')

df1.to_csv(f"merged{SET}.csv", index=False)