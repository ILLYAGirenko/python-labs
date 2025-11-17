import matplotlib.pyplot as plt
import numpy as np

data_json = [
    {
        "name": "Ukraine",
        "area": 603700,
        "population": 40000000,
        "continent": "Europe"
    },
    {
        "name": "Egypt",
        "area": 1002000,
        "population": 109000000,
        "continent": "Africa"
    },
    {
        "name": "China",
        "area": 9597000,
        "population": 1412000000,
        "continent": "Asia"
    },
    {
        "name": "Germany",
        "area": 357000,
        "population": 84000000,
        "continent": "Europe"
    },
    {
        "name": "Kenya",
        "area": 580000,
        "population": 55000000,
        "continent": "Africa"
    },
    {
        "name": "Japan",
        "area": 378000,
        "population": 124000000,
        "continent": "Asia"
    },
    {
        "name": "Brazil",
        "area": 8516000,
        "population": 214000000,
        "continent": "South America"
    },
    {
        "name": "Australia",
        "area": 7692000,
        "population": 26000000,
        "continent": "Australia"
    },
    {
        "name": "India",
        "area": 3287000,
        "population": 1393000000,
        "continent": "Asia"
    }
]

countries = [item["name"] for item in data_json]
populations = [item["population"] for item in data_json]
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))

def func(pct, allvals):
    absolute = int(np.round(pct / 100.0 * np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:,})"

wedges, texts, autotexts = ax.pie(
    populations,
    autopct=lambda pct: func(pct, populations),
    textprops=dict(color="white")
)
ax.legend(
    wedges,
    countries,
    title="Countries",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)
plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Розподіл населення по країнах")
plt.show()