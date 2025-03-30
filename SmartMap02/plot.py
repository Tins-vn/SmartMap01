import matplotlib.pyplot as plt

def scatter_map(X, Y, name):

    plt.scatter(X[1:],Y[1:])

    plt.xlim(0, 600)
    plt.ylim(0, 600)

    for i in range(len(X[1:])):
        plt.annotate(name[i+1], (X[i+1], Y[i+1]), 
                    fontsize=7, ha="center", va="bottom",
                    textcoords="offset points", xytext=(0, 5)) 

    plt.axhline(y = 300 , color='black', linewidth = 1, alpha = 0.3)
    plt.axvline(x = 300 , color='black', linewidth = 1, alpha = 0.3)

    plt.show()
