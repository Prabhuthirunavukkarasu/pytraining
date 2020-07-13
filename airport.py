"""
module defs
"""
small_airports = []
large_airports = []
medium_airports = []
others = []
helipads = []
def get_file(filename):
    """
    function defs
    """
    opened_file = open(file=filename, mode='rt', encoding='utf-8')
    row = opened_file.readline()
    while row:
        row = opened_file.readline()
        row = row.replace("\"", "")
        if len(row) != 0:
            cols = row.split(",")
            if(cols[2] == 'small_airport'):
                small_airports.append(cols[3])
            elif(cols[2] == 'medium_airport'):
                medium_airports.append(cols[3])
            elif(cols[2] == 'large_airport'):
                large_airports.append(cols[3])
            elif(cols[2] == 'heliport'):
                helipads.append(cols[3])
            else:
                others.append(cols[3])
get_file('C:/Users/Administrator/Downloads/airports.csv')
print("**LARGE AIRPORTS**")
print(len(large_airports))
print("**MEDIUM AIRPORTS**")
print(len(medium_airports))
print("**SMALL AIRPORTS**")
print(len(small_airports))
print("**HELIPADS**")
print(len(helipads))
print("**OTHERS**")
print(len(others))
