# pp 38 - 39

#import numpy as np

#jeff_salary = [2700,3000,3000]
#nick_salary = [2600,2800,2800]
#tom_salary = [2300,2500,2500]
#base_salary = np.array([jeff_salary, nick_salary, tom_salary])
#print(base_salary)  
#jeff_bonus = [500,400,400]
#nick_bonus = [600,300,400]
#tom_bonus = [200,500,400]
#bonus = np.array([jeff_bonus, nick_bonus, tom_bonus])
#salary_bonus = base_salary + bonus
#print(type(salary_bonus))
#print(salary_bonus)


import numpy as np

# Define base salaries and bonuses in a more compact way
base_salary = np.array([
    [2700, 3000, 3000],  # Jeff's salary
    [2600, 2800, 2800],  # Nick's salary
    [2300, 2500, 2500]   # Tom's salary
])

bonus = np.array([
    [500, 400, 400],     # Jeff's bonus
    [600, 300, 400],     # Nick's bonus
    [200, 500, 400]      # Tom's bonus
])

# Calculate total salary by adding base salary and bonus
salary_bonus = base_salary + bonus

print(type(salary_bonus))
print(salary_bonus)