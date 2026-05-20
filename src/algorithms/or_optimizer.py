from ortools.linear_solver import pywraplp

def optimize_settlements(balances):
    debtors = {node: -amount for node, amount in balances.items() if amount < 0}
    creditors = {node: amount for node, amount in balances.items() if amount > 0}

    # print(debtors, creditors)

    solver = pywraplp.Solver.CreateSolver("SCIP")

    # Decision Variables
    x = {}

    for debtor in debtors:
        for creditor in creditors:
            x[(debtor, creditor)] = solver.NumVar(
                0,
                solver.infinity(),
                f"x_{debtor}_{creditor}"
            )

    # print("x:", x)

    # Debtor constraints
    for debtor, amount in debtors.items():
        solver.Add(
            # `sum` combines multiple decision variables into ONE equation
            sum(x[debtor, creditor] for creditor in creditors) == amount
        )

    # Creditor constraints
    for creditor, amount in creditors.items():
        solver.Add(
            sum(x[debtor, creditor] for debtor in debtors) == amount
        )

    # Objective
    solver.Minimize(
        sum(x[debtor, creditor] for debtor in debtors for creditor in creditors)
    )

    status = solver.Solve()

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