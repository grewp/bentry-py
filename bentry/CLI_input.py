import datetime

def getItem():
    item = raw_input("item: ")

    if item.isalpha():
        return item
    else:
        print 'Invalid input'
        return getItem()

def getCost():
    cost = raw_input("cost: ")

    try:
        cost = float(cost)
        return cost
    except ValueError:
        print("Invalid input")
        return getCost()

def getCategory():
    category = raw_input("category (F/E/T/M): ").upper()

    categoryShorthand = {'F': 'Food', 'E': 'Entertainment', 'T': 'Transportation', 'M': 'Misc'}

    if category in ('F', 'E', 'T', 'M'):
        return categoryShorthand[category]
    else:
        print "Invalid input"
        return getCategory()

def getDate():
    date = raw_input('date MM/DD (optional): ')

    if date == '':
        return datetime.date.today()
    else:
        try:
            date = datetime.datetime.strptime(date, '%m/%d').replace(year=datetime.date.today().year).date()
            return date
        except:
            print 'Invalid input'
            return getDate()

def getEntry():
    item = getItem()
    cost = getCost()
    category = getCategory()
    date = getDate()
    return {'name': item, 'price': cost, 'category': category, 'date': date}

def userInput():
    """collects user input on startup"""
    print "Welcome to budget entry. To begin press enter, or press ctrl+C to quit at any time"

    entries=[]
    entries.append(getEntry())

    entering_items = True
    while entering_items:
        continue_entering = raw_input("enter another item? (Y/N)").lower()

        if continue_entering == 'y':
            entries.append(getEntry())
        elif continue_entering == 'n':
            break
        else:
            print 'Invalid input. Please retry'

    return entries
