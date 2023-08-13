def linreg(x, y, x_label, y_label, title):
    #import dependencies required for function.
    from scipy.stats import linregress
    import matplotlib.pyplot as plt
    import numpy as np
    
    #Calculate the linear regression line
    slope, intercept, r_val, p_val, std_err = linregress(x, y)
    best_fit = slope * x + intercept
    
    #need to print the line equation   
    line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
    
    #Plot the scatter
    plt.scatter(x,y)

    # Set x-axis limits and ticks based on input x values
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    plt.xlim(x_min, x_max)
    plt.xticks(np.arange(x_min, x_max+1, 5))
    
    #Plot the line equation at bottom right of graph
    plt.annotate(line_eq, (x_max,y_min), fontsize=15, color="red",
                 horizontalalignment='right', verticalalignment='bottom')
    
    #Plot the best fit line
    plt.plot(x,best_fit,"r-")
    
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    return plt.show(), print(f'The r-value is: {r_val}')