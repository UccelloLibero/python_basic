TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:

    print("There are {} tickets remaining.".format(tickets_remaining))

    first_name = input("Hi. What is your name? ")

    number_of_tickets = input("How many tickets would you like, {}? ".format(first_name))

    try:
        number_of_tickets = int(number_of_tickets)

        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("That was not a valid value you entered. {} Please try again.".format(err))

    else:
        amount_due = calculate_price(number_of_tickets)
        print("The total due is ${}.".format(amount_due))
        proceed = input("Would you like to proceed? Y/N ")

        if proceed.lower() == "y":
            # TODO: Gather credit card information and process it
            print("SOLD!!!")

            tickets_remaining -= number_of_tickets
        else:
            print("Thank you anyway, {}.".format(first_name))

print("All sold out!")
