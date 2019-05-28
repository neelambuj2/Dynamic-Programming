def maxMin(operations, x):
    main_stack = []
    min_stack = []
    max_stack = []
    min_stack.append(x[0])
    max_stack.append(x[0])
    main_stack.append(x[0])
    res =[]
    res.append(min_stack[-1] * max_stack[-1])
    for oper in range(1, len(operations)):
        main_stack.append(x[oper])
        if operations[oper] == "push":
            if x[oper] < min_stack[-1]:
                min_stack.append(x[oper])
            if x[oper] > max_stack[-1]:
                max_stack.append(x[oper])
        if operations[oper] == "pop":
            top = main_stack.pop()
            if top == min_stack[-1]:
                min_stack.pop()
            if top == max_stack[-1]:
                max_stack.pop()
        if not min_stack:
            j=0
            while min_stack[j] ==
            res.append(max_stack[0]*max_stack[-1])
        elif not max_stack:
            res.append(min_stack[0]*min_stack[-1])
        else:
            res.append(min_stack[-1] * max_stack[-1])
    return res

x = [1, 2, 3, 1]
operations = ["push","push","push", "pop"]
print(maxMin(operations,x))
