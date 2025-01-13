# mathematical set operations

# sets
engineers = {'Siddharth', 'Nitin', 'Savio', 'Tejas', 'Sohel', 'Neeraj', 'Alex'}
managers = {'Faizan', 'Sunny', 'Rohit', 'Krutika', 'Kishan', 'Pratik', 'Savio', 'Alex'}
ceo = {'Alex'}

# union - all people in all 3 categories
print(engineers | managers | ceo)

# intersection -

# who are engineers and managers
print(engineers & managers)
# who are engineers, managers, and ceos
print(engineers & managers & ceo)

# difference - 

# engineers who are not managers
print(engineers - managers)

# managers who are not engineers
print(managers - engineers)

# symmetric difference - 
# managers who are not engineers
# and engineers who are not managers
# prints only the unique values 
# i.e. values which are not common between both the sets
print(managers ^ engineers)
