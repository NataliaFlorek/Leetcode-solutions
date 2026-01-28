import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    pick_false =customers["id"].isin(orders["customerId"])
    return customers.loc[~pick_false][["name"]].rename(columns={"name":"Customers"})