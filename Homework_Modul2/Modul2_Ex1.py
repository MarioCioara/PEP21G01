# 1) Prove "and" operation takes precedence over "or" operation by setting
# parentheses in the following expression (False or False and True or True)


#By setting up the two Trues between parantheses we changed the outcome of the expression to False
#The expression is now False because,now,the second OR is done before the AND due to the parantheses
print(False or False and (True or True))