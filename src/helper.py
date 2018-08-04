
def validate_line(ID, lastName, firstName, drugName, drugCost):
    if not isint(ID):
        return False
    #if not lastName.isupper():
        #return False
    #if not firstName.isupper():
        #return False
    #if not drugName.isupper():
        #return False
    if not isfloat(drugCost):
        return False
    
    return True

# To validate a float value
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# To validate a int value    
def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


