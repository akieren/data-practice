import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Sales': [250, 300, 280, 350, 400]
    }
    df = pd.DataFrame(data)

    print("Data Overview:")
    print(df)

    plt.plot(df['Year'], df['Sales'])
    plt.title('Sales Over Years')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.show()

if __name__ == "__main__":
    main()
