def unify(pattern, fact, theta):
    if len(pattern) != len(fact) or pattern[0] != fact[0]:
        return None

    theta = theta.copy()

    for p, f in zip(pattern[1:], fact[1:]):
        if p.startswith("?"):
            if p in theta and theta[p] != f:
                return None
            theta[p] = f
        elif p != f:
            return None

    return theta


def matching_subs(premises, facts, theta):
    if not premises:
        yield theta
        return

    for fact in facts:
        s = unify(premises[0], fact, theta)

        if s is not None:
            yield from matching_subs(premises[1:], facts, s)


def subst(theta, q):
    return (q[0], *(theta.get(x, x) for x in q[1:]))


def fol_fc_ask(facts, rules, alpha):
    for fact in facts:
        psi = unify(alpha, fact, {})
        if psi is not None:
            return psi

    while True:
        new = []

        for premises, q in rules:
            for theta in matching_subs(premises, facts, {}):
                q1 = subst(theta, q)

                if q1 not in facts and q1 not in new:
                    new.append(q1)
                    print("New fact:", q1)

                    psi = unify(alpha, q1, {})

                    if psi is not None:
                        return psi

        if not new:
            return False

        facts.extend(new)


# Convert input into tuple
def parse(s):
    s = s.replace("(", " ").replace(")", "")
    s = s.replace(",", " ")
    return tuple(s.split())


# User input for facts
facts = []
n = int(input("Enter number of facts: "))

for i in range(n):
    facts.append(parse(input("Enter fact: ")))


# User input for rules
rules = []
n = int(input("Enter number of rules: "))

for i in range(n):
    rule = input("Enter rule: ")
    lhs, rhs = rule.split("->")

    premises = [parse(p) for p in lhs.split("&")]
    conclusion = parse(rhs)

    rules.append((premises, conclusion))


# User input for query
alpha = parse(input("Enter query: "))

result = fol_fc_ask(facts, rules, alpha)

if result is False:
    print("Query cannot be inferred")
else:
    print("Query is satisfied")
    print("Substitution:", result)