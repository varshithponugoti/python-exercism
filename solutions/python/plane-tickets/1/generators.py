"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    LETTERS = ["A","B","C","D"]

    index = 0
    while index < number:
        yield LETTERS[index % 4]
        index+=1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For exampl: 3C, 3D, 4A, 4B

    """
    digit = 0
    for letter in generate_seat_letters(number):
        if letter == "A":
            digit+=1
        if digit == 13:
            digit+=1
        yield str(digit)+letter
            
        

def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    index = 0
    number = len(passengers)
    assigned_seats = {}
    for seat in generate_seats(number):
        assigned_seats[passengers[index]]=seat
        index+=1
    return assigned_seats

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    CODE_LENGTH = 12
    for seat in seat_numbers:
        ticket_id = seat+flight_id
        yield ticket_id+"0"*(CODE_LENGTH-len(ticket_id))
