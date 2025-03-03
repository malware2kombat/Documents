'''BLUE imports:
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
'''
#Line Plot "Attack Trends Over Time"
def bluelineplot():
    x = np.arrange(10) # Time (hours)
    y = np.random.randit(10, 50, size=10) # Number of attacks
    plt.plot(x, y, 
            marker='o', linestyle='-', 
            color='b',label="failed Logins")
    
    plt.xlabel("Time (Hours)") 
    plt.ylabel("Number of Attacks")
    plt.title("Failed Login Attempts Over Time")
    
    plt.legend()
    plt.show()
