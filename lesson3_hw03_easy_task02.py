def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    ticket_part1 = ticket_number[:len(ticket_number)//2]
    ticket_part2 = ticket_number[len(ticket_number)//2:]
    if sum(map(int, str(ticket_part1))) == sum(map(int, str(ticket_part2))):
        return ticket_number

print(lucky_ticket(123006))
print(lucky_ticket(123217))
print(lucky_ticket(436751))

