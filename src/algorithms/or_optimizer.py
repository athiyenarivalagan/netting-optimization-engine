from ortools.linear_solver import pywraplp

def optimize_settlements(balances):
    debtors = {node: -amount for node, amount in balances.items() if amount < 0}
    creditors = {node: amount for node, amount in balances.items() if amount > 0}

    # print("\nDebtors", debtors, "Creditors:", creditors)

    solver = pywraplp.Solver.CreateSolver("SCIP")

    # Decision Variables:
    x = {}
    y = {}

    # create variables
    for debtor in debtors:
        for creditor in creditors:
            x[(debtor, creditor)] = solver.NumVar(
                0,
                solver.infinity(),
                f"x_{debtor}_{creditor}"
            )

            y[(debtor, creditor)] = solver.BoolVar(
                f"y_{debtor}_{creditor}"
            )

    # print("\nx:", x)
    # print("\ny:", y)


    # Debtor constraints
    for debtor, amount in debtors.items():
        # print(
        #     "\ndebtor constraint:", 
        #     sum(x[(debtor, creditor)] for creditor in creditors) == amount
        # )
        solver.Add(
            # `sum` combines multiple decision variables into ONE equation
            sum(x[(debtor, creditor)] for creditor in creditors) == amount
        )

    # Creditor constraints
    for creditor, amount in creditors.items():
        # print(
        #     "\ncreditor constraint:", 
        #     sum(x[(debtor, creditor)] for debtor in debtors) == amount
        # )
        solver.Add(
            sum(x[(debtor, creditor)] for debtor in debtors) == amount
        )


    # Big-M linking constraints
    M = sum(creditors.values())
    # print("\nM:", M)
    
    for debtor in debtors:
        for creditor in creditors:
            # print("\nlinking constraint:", x[(debtor, creditor)] <= M * y[(debtor, creditor)])
            solver.Add(
                    x[(debtor, creditor)] <= M * y[(debtor, creditor)] 
            )

    # Objective:
    #
    # print("\nObjective:", sum(x[debtor, creditor] for debtor in debtors for creditor in creditors))  
    # solver.Minimize(
    #     sum(x[debtor, creditor] for debtor in debtors for creditor in creditors)
    # )
    # print("Objective:", sum(y[(debtor, creditor)] for debtor in debtors for creditor in creditors))
    # Minimize number of active transactions.
    # The solver now tries to deactivate as many edges as possible.
    solver.Minimize(
        sum(y[(debtor, creditor)] for debtor in debtors for creditor in creditors)
    )

    status = solver.Solve()

    # Result
    if status == pywraplp.Solver.OPTIMAL:
        settlements = []

        for debtor in debtors:
            for creditor in creditors:
                amount = x[(debtor, creditor)].solution_value()

                if amount > 1e-6:
                    settlements.append((debtor, creditor, amount))

        # print("Optimized settlements:")
        # for debtor, creditor, amount in settlements:
        #     print(f"{debtor} -> {creditor}: {amount}")

        return settlements

    else:
        print("No solution found")
        return []