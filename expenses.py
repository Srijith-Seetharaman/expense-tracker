expenses = {}
new_expense_input_mapping = {
    True: ["True", "Yes", "Y"],
    False: ["False", "No", "N"],
}


def ask_yes_or_no_question(question: str, list: dict[bool, list[str]]):
    possible_values = []

    for key in list.keys():
        for each_key in list[key]:
            possible_values.append(each_key.lower())

    counter = 0
    do_you_wanna_add_new_expense = None
    while do_you_wanna_add_new_expense not in possible_values:
        if counter > 0:
            print(f"That's not the right response. Try again")
        do_you_wanna_add_new_expense = input(f"{question} ").lower()
        counter += 1
    if do_you_wanna_add_new_expense in new_expense_input_mapping[True]:
        return True
    else:
        return False


def push_expense_to_tracker(expense_item: str, amount: int) -> None:
    maxValue = 0
    for value in expenses.keys():
        if value > maxValue:
            maxValue = value
    newIndex = maxValue + 1
    expenses[newIndex] = {
        "expenseItem": expense_item,
        "expenseAmount": f"${str(amount)}",
    }


def display_all_expenses() -> None:
    for key, value in expenses.items():
        expenseItem = value["expenseItem"]
        expenseAmount = value["expenseAmount"]
        print(key, expenseItem, expenseAmount)
