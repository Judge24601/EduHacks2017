#!/usr/bin/python

#collection of all basic gate functions defined
#take one-two boolean inputs and returns a boolean output

#basic NOT gate function (~A)
def NOT(self, inputA):
    if inputA == True:
        return False
    else:
        return True:

#basic AND gate function (A&B)
def AND(self, inputA, inputB):
    if inputA == True && inputB == True:
        return True
    else:
        return False

#basic OR gate function (AvB)
def OR(self, inputA, inputB):
    if inputA == True:
        return True
    elif inputB == True:
        return True
    else:
        return False

#basic NOR (neither) gate function (~(AvB))
def NOR(self, inputA, inputB):
    if inputA == True:
        return False
    elif inputB == True:
        return False
    else:
        return True

#basic NAND (not both) gate function (~(A&B))
def NAND(self, inputA, inputB):
    if inputA == True && inputB == True:
        return False
    else:
        return True

#basic XNOR (equality) gate function ((~A&~B)v(A&B))
def NAND(self, inputA, inputB):
    if inputA == inputB:
        return True
    else:
        return False

#basic XOR (exclusive or) gate function (~((~A&~B)v(A&B)))
def NAND(self, inputA, inputB):
    if inputA == inputB:
        return False
    else:
        return True
