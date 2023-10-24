import numpy as np
def graident_descent(x,y):
    m_current = b_current = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.08
    for i in range(iterations):
        #prediction 
        y_predicted = m_current * x + b_current 
        #cost
        cost = (1/n) * sum([val ** 2 for val in (y-y_predicted)])
        #partial deritivtives equations
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        #update m_current 
        m_current = m_current - learning_rate * md
        b_current = b_current - learning_rate * bd
        print(f"m: {m_current}, b: {b_current}, iteration: {i}, cost: {cost} ")

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

graident_descent(x,y)


  

