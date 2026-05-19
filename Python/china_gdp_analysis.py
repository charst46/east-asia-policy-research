import wbgapi as wb
import pandas as pd

# Pull China GDP data from World Bank
df = wb.data.DataFrame('NY.GDP.MKTP.CD', 'CHN')

# Convert to readable trillions
df_clean = df.T
df_clean.columns = ['GDP_USD']
df_clean['GDP_Trillions'] = df_clean['GDP_USD'] / 1e12
df_clean.index = df_clean.index.str.replace('YR', '')

# Show last 10 years
print(df_clean['GDP_Trillions'].tail(10))

# Analysis notes:
# Two plateaus identified:
# Plateau 1: 2018-2020, $14.1T to $15.0T (+$800B)
# Plateau 2: 2021-2024, $18.2T to $18.7T (+$500B)
# 2023 contraction of ~$46B consistent with Minsky debt cycle hypothesis
# Property sector speculative debt (Evergrande etc.) produced classic Ponzi-to-contraction dynamic
