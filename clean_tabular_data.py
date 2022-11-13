import pandas as pd

fb_products = pd.read_csv("products.csv", lineterminator="\n")

fb_products["price"] = fb_products["price"].str.strip("£")
fb_products["price"] = fb_products["price"].str.replace(",", "")
fb_products["price"] = fb_products["price"].astype("float64")

fb_products.to_csv("products_cleaned.csv", lineterminator="\n")