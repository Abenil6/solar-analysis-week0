import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def compare_metrics():
    benin = pd.read_csv("data/cleaned/benin.csv")
    togo = pd.read_csv("data/cleaned/togo.csv")
    sierra = pd.read_csv("data/cleaned/sierraleone.csv")

    benin["Country"] = "Benin"
    togo["Country"] = "Togo"
    sierra["Country"] = "Sierra Leone"

    df = pd.concat([benin, togo, sierra])

    sns.boxplot(x="Country", y="GHI", data=df)
    plt.title("GHI Comparison")
    plt.show()
