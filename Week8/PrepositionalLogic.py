def tt_entails(kb, alpha, symbols):
    return tt_check_all(kb, alpha, symbols, {})


def tt_check_all(kb, alpha, symbols, model):
    if not symbols:
        if eval(kb, {"__builtins__": {}}, model):
            return eval(alpha, {"__builtins__": {}}, model)
        else:
            return True

    p = symbols[0]
    rest = symbols[1:]

    return (
        tt_check_all(kb, alpha, rest, {**model, p: True})
        and
        tt_check_all(kb, alpha, rest, {**model, p: False})
    )


# User input
symbols = input("Enter propositional symbols: ").split()
kb = input("Enter knowledge base: ")
alpha = input("Enter query: ")

result = tt_entails(kb, alpha, symbols)

if result:
    print("KB entails the query: True")
else:
    print("KB entails the query: False")