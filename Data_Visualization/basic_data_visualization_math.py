#!/usr/bin/env python
# coding: utf-8

# Digital Scholarship Tools  
# 2020  
# Author: Michael Horn

# # Basic Data Visualization Procedures: Mathematical Functions

# In this Notebook we will present some basic methods to visualize data for mathematical functions.

# Libraries required:

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# First, we will generate some data by defining a mathematical function. As an example, lest`s take a polynomial function like f(x) = 2x<sup>3</sup> + x<sup>2</sup> + 3x + 5.

# In[3]:


# The function "polynom" takes a list of x-values as input and returns a list of y-values as output.
def polynom(list_x_values):
    list_y_values = []
    for x_value in list_x_values:
        y_value = 2* x_value**3 + x_value**2 + 3*x_value + 5
        list_y_values.append(y_value)
    return list_y_values


# In[4]:


# We generate a list of x-values by starting with an empty list and gradually adding integer values from -10 to 10.
list_x_values = []

for number in range (-10, 11):
    list_x_values.append(number)


# In[5]:


print(list_x_values)


# Now we apply the function "polynom" to the list of x-values we just generated.

# In[6]:


list_y_values = polynom(list_x_values)


# The result is a list of corresponding y-values:

# In[7]:


print(list_y_values)


# With **matplotlib** we can visualize the data saved in the two lists. By default we obtain the following scatter-plot, which shows the locations of the data points.

# In[8]:


plt.scatter(list_x_values, list_y_values)
plt.show()


# An alternative is to plot a line instead of showing the points:

# In[9]:


plt.plot(list_x_values, list_y_values)
plt.show()


# We can plot the two diagrams next to each other in a figure:

# In[10]:


plt.figure(figsize = (14,4))
plt.subplot(1,2,1)
plt.scatter(list_x_values, list_y_values)
           
plt.subplot(1,2,2)
plt.plot(list_x_values, list_y_values)

plt.show()


# The default representation of the data is ok, but one can generate much nicer plots. Let's do that by changing some parameters for the line-plot:

# In[11]:


# Defines the size of the figure:
plt.figure(figsize = (8,6))

# Defines the plot-type, in this case a line-plot. Takes the data to be plotted. "Linewith" defines the thickness of 
# the plotted line, "color" the line-colour, "marker" adds additional marks to the plot and "markevery" defines the 
# locations of these markers. 
# In our case, we mimick a mixture of a line-plot and a scatter-plot by setting marker at the places, where our data points 
# are located.
plt.plot(list_x_values, list_y_values, linewidth = 2, color="red", marker="o", markevery=1)

# A diagram should have a title, so we give it one:
plt.title("f(x) = 2$x^3$ + $x^2$ + 3x + 5 \n", fontsize=20, color="black")

# The x- and y-axes should be labelled, so we label them:
plt.xlabel("Value for x", fontsize=20)
plt.ylabel("Value for f(x)", fontsize=20)

# We can specify, which values to show on the x- and y-axes. This we do by defining the "ticks" and including some parameters
# for their appearance.
plt.xticks([-10, -5, 0, 5, 10])
plt.yticks([-2000, -1000, 0, 1000, 2000])
plt.tick_params(axis="x", labelsize=18)
plt.tick_params(axis="y", labelsize=14)

# Gridlines can facilitate data interpretation. We include them at the positions of the ticks and define their appearance.
plt.grid(True, color="gray", linestyle="--", linewidth=1)

# In the default data-representation, the x=0 and y=0 axes were not shown. We include these axes in our diagram 
plt.axhline(y=0, linewidth=2, color="black")
plt.axvline(x=0, linewidth=2, color="black")

plt.show()


# Let`s add some additional data to our figure. We define a second function, let's say f(x) = - (2x<sup>3</sup> + x<sup>2</sup> + 3x + 5) and generate the according list of y-values.  

# In[12]:


def neg_polynom(list_x_values):
    list_y_values = []
    for x_value in list_x_values:
        y_value = - (2* x_value**3 + x_value**2 + 3*x_value + 5)
        list_y_values.append(y_value)
    return list_y_values


# In[13]:


neg_y_values = neg_polynom(list_x_values)
print(neg_y_values)


# We plot both data sets to the same figure and label them accordingly.

# In[14]:


# Defines the size of the figure:
plt.figure(figsize = (8,6))

# Defines the plot-type, in this case a line-plot. Takes the data to be plotted. "Linewith" defines the thickness of 
# the plotted line, "color" the line-colour, "marker" adds additional marks to the plot and "markevery" defines the 
# locations of these markers. 
# In our case, we mimick a mixture of a line-plot and a scatter-plot by setting marker at the places, where our data points 
# are located.
plt.plot(list_x_values, list_y_values, linewidth = 2, color="red", marker="o", markevery=1)

plt.plot(list_x_values, neg_y_values, linewidth = 2, color="blue", marker="o", markevery=1)

# For a title with multiple colours wie use the method "figtext". The numbers in front of each text string represent the x- and
# y-coordinates for the position of each text string
plt.figtext(0.3, 1, "f(x) =    2$x^3$ + $x^2$ + 3x + 5", fontsize=20, color="red") 
plt.figtext(0.3, 0.92, "f(x) = - (2$x^3$ + $x^2$ + 3x + 5)", fontsize=20, color="blue")

# The x- and y-axes should be labelled, so we label them:
plt.xlabel("Value for x", fontsize=20)
plt.ylabel("Value for f(x)", fontsize=20)

# We can specify, which values to show an the x- and y-axes. This we do by defining the "ticks" and including some parameters
# for their appearance.
plt.xticks([-10, -5, 0, 5, 10])
plt.yticks([-2000, -1000, 0, 1000, 2000])
plt.tick_params(axis="x", labelsize=18)
plt.tick_params(axis="y", labelsize=14)

# Gridlines can facilitate data interpretation. We include them at the positions of the ticks and define their appearance.
plt.grid(True, color="gray", linestyle="--", linewidth=1)

# In the default data-representation, the x=0 and y=0 axes were not shown. We include these achses in our diagram 
plt.axhline(y=0, linewidth=2, color="black")
plt.axvline(x=0, linewidth=2, color="black")

plt.show()


# In[ ]:




