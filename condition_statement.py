"""syntax:

    if <expression> [logical][expression_2]:
    >>>>true block block_start
    <<<<


    if <expression> [logical][expression_2]:
    >>>>true block block_start
    <<<<
    else:
    >>>>false block block_start
    <<<<

    
    if <expression> [logical][expression_2]:
    >>>>true block block_start
    <<<<
    elif <expression> [logical][expression_2]:
    >>>>else if block
    <<<<
    else:
    >>>>false block block_start
    <<<<
    
    """

name="nivetha"
dept="intern"

if(name=="nivetha" and dept=="intern"):
   print("entry allowed")
else:
    print("entry restricted")
