import numpy as np
import matplotlib.pyplot as plt

x=[2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
y=[2.3,2.1,2.0,1.7,1.9,1.6,1.5,1.6,1.1, 0.6, 0.9,0.9,1.2,0.9,1.7,1.1,0.9,1.0,1.2,1.5] #Germany
z=[2.0, 8.1,8.2,7.7,7.7,7.6,7.6,8.1,8.4,9.1,10.2,10.7,11.3,16.0,16.3,16.5,16.8,16.4,16.3,15.9] #Ukraine
np.array(x)
np.array(y)
np.array(z)
plt.plot(x,y, label='Germany', color='blue')
plt.plot(x,z, label='Ukraine', color='green')
plt.xticks(x)
plt.title("Children out of school (% of primary school age)")
plt.xlabel('Year', fontsize=12,color='red')
plt.ylabel('Indicator, %', fontsize=12,color='red')
plt.xticks(x)
plt.legend()
plt.grid(True)
plt.show()

country=input("Введіть країну для побудови стовпчастої діаграми(Германія/Україна): ")
if country == "Германія":
    values = y
elif country == "Україна":
    values =z
else:
    print("Такої країни не запропоновано дял вибору")
    exit()
plt.figure(figsize=(10, 5))
plt.bar(x, values)
plt.xticks(x, rotation=45)
plt.title(f"Children out of school (%): {country}")
plt.xlabel("Year")
plt.ylabel("Indicator, %")
plt.grid(axis='y')
plt.show()