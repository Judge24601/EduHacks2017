//collection of all basic gate functions defined
//take one-two boolean inputs and returns a boolean output

//basic NOT gate function (~A)
function not(inputA){
    if inputA == True {
        return false;
    } else{
        return true;
    }
}

//basic AND gate function (A&B)
function and(inputA, inputB){
    if inputA == true && inputB == true;
        return true;
    } else{
        return false;
}
//basic OR gate function (AvB)
function or(inputA, inputB){
    if inputA == true{
        return true;
    } else if inputB == true:
        return true;
    } else{
        return false;
    }
}
//basic NOR (neither) gate function (~(AvB))
function nor(inputA, inputB){
    if inputA == true{
        return false;
    } else if inputB == true{
        return false;
    } else{
        return true;
    }
}
//basic NAND (not both) gate function (~(A&B))
function nand(inputA, inputB){
    if inputA == true && inputB == true{
        return false;
    } else{
        return true;
    }
}

//basic XNOR (equality) gate function ((~A&~B)v(A&B))
function xnor(inputA, inputB){}
    if inputA == inputB{
        return true;
    } else{
        return false;
    }
}
//basic XOR (exclusive or) gate function (~((~A&~B)v(A&B)))
def xor(inputA, inputB){
    if inputA == inputB{
        return false;
    } else{
        return true;
    }
}
