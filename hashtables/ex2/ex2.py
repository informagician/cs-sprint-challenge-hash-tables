#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    path = {}
    for ticket in tickets:
        path[ticket.source] = ticket.destination
    print(path)

    res = []
    res.append(path['NONE'])

    for i in range(len(path) - 1):
        res.append(path[res[i]])

    return res
