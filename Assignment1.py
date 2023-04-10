# add import of pulp and other things you need here
import pulp
from pulp import *

def ex1():
    retval = {}
    retval["x"] = None
    retval["y"] = None
    retval["obj"] = None
    retval["tight_constraints"] = [ None ]
    # Insert your code below:

    x = LpVariable("x", -10, None)
    y = LpVariable("y", None, 10)
    prob = LpProblem("problem", LpMinimize)

    prob += 122*x + 143*y

    prob += 3*x + 2*y <= 10
    prob += 12 * x + 14 *y >= -12.5 
    prob += 2*x + 3*y >= 3
    prob += 5*x - 6*y >= -100
    


    sol = prob.solve(PULP_CBC_CMD(msg = 0))

   
    def check_if_tight():
        retval["tight_constraints"] = []
        i = 0
        for c in prob.constraints:
            i += 1
            if prob.constraints[c].value()==0:
                 retval["tight_constraints"].append(i)
           

    
    retval["x"] = value(x)
    retval["y"] = value(y)
    retval["obj"] = value(prob.objective)
    check_if_tight()
    
    # Return retval dictionary
    return retval


def ex2():
    retval = {}
    retval['x1'] = None
    retval['x2'] = None
    retval['x3'] = None
    retval['x4'] = None
    retval['x5'] = None
    retval['x6'] = None
    retval['obj'] = None
    # Insert your code below:
    
    x0 = LpVariable("0")
    x1 = LpVariable("1", 0, None)
    x2 = LpVariable("2", 0, None)
    x3 = LpVariable("3", 0, None)
    x4 = LpVariable("4", 0, None)
    x5 = LpVariable("5", 0, None)
    x6 = LpVariable("6", 0, None)

    prob = LpProblem("problem", LpMinimize)

    prob += x0

    prob += x0 >= 2*x2 - x3 - x4 - x5- x6
    prob += x0 >= -2*x1 + 2*x3 - x4- x5 - x6
    prob += x0 >= x1 - 2*x2 + 2*x4 -x5 - x6
    prob += x0 >= x1 + x2 - 2*x3 + 2*x5 -x6
    prob += x0 >= x1 + x2 +x3 - 2*x4 + 2*x6
    prob += x0 >= x1 +x2 +x3 +x4 - 2*x5

    prob += x1 + x2 + x3 + x4 + x5 + x6 == 1

    sol = prob.solve(PULP_CBC_CMD(msg = 0))
    
    retval["x1"] = value(x1)
    retval["x2"] = value(x2)
    retval["x3"] = value(x3)
    retval["x4"] = value(x4)
    retval["x5"] = value(x5)
    retval["x6"] = value(x6)
    retval["obj"] = value(prob.objective)
    # return retval dictionary
    return retval


def ex3():
    retval = {}
    retval['obj'] = None
    retval['x1'] = None
    # there should be retval['xi'] for each company number i
    # Insert your code below:
    
    f = open("hw1-03.txt", "r")
    x = []
    for t in f:
        x.append(t.split())        



    y = LpVariable.dicts("x",[str(i+1) for i in range(69)], lowBound=0)
    reps = lpSum(y[name] for name in y.keys())


    prob = LpProblem("problem", LpMinimize)

    prob += reps
    
    for i in range(len(x)):
        prob += y[x[i][0]]+y[x[i][1]] >= 2 

    sol = prob.solve(PULP_CBC_CMD(msg = 0))

    f.close()
    
    retval["obj"] = value(prob.objective)
    for i in range(69):
        retval["x"+str(i+1)] = value(y[str(i+1)])
        
    # return retval dictionary
    return retval
