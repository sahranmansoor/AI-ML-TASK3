import pandas as pd

def main():
    df = pd.read_csv("Housing.csv")

    area_limit = df["area"].quantile(0.9)
    price_limit = df["price"].quantile(0.9)
    
    df = df[(df["area"] <= area_limit) & (df["price"] <= price_limit)]

    df["furnishingstatus"] = df["furnishingstatus"].map({
        "furnished": 2,
        "semi-furnished": 1,
        "unfurnished": 0
        })
    nncs = df.select_dtypes(exclude="number").columns.tolist()

    for c in nncs:
        df[c] = df[c].map({ "yes": 1, "no": 0})

    df.to_csv("Housing_processed.csv", index=False)

if __name__ == "__main__":
    main()
