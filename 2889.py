import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivoted=pd.pivot_table(weather, index='month', columns='city', values='temperature', aggfunc='sum')
    return pivoted