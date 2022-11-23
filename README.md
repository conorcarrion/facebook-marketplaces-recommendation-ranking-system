# Facebook Market-Place's Recommendation Ranking System Documentation

This project aims to emulate the system used by Facebook Market-Place's Recommendation Ranking System. By doing so I aim to learn about Machine learning techniques.

Technologies used:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg) 
![Pillow](https://img.shields.io/badge/Pillow-blueviolet?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) 
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)  
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) 
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)  
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


## Milestone 1, 2 & 3 - Setting up the environment and exploring the dataset

I was provided with the following files to begin the project:
    1. products.csv - a table of the information for each product listing
    2. images.csv - a table containing the list of products and which product information they relate to
    3. images folder - containing 12668 images of the products

I began by cleaning the products csv. I opened the file using Pandas library, removed the currency symbol £ and comma (,) from the price column and converted the column type to float. I then wrote the resulting table to a new csv file with the same delimiter (line break "\n"). 


```python
"""import pandas as pd

fb_products = pd.read_csv("products.csv", lineterminator="\n")

fb_products["price"] = fb_products["price"].str.strip("£")
fb_products["price"] = fb_products["price"].str.replace(",", "")
fb_products["price"] = fb_products["price"].astype("float64")

fb_products.to_csv("products_cleaned.csv", lineterminator="\n")""
```

For the second task I cleaned the image dataset. I wanted the pictures to all be the same size (512 * 512) and RGB.


## Milestone 4