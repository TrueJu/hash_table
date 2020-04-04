def convert2DECSum(inpStr):     # Takes in any string and returns the sum of the hash values of each char
    inpStr = str(inpStr)
    _tmp_ = 0
    for num in range(len(inpStr)):
        _tmp_ += ord(inpStr[num])   # Getting the char's hash value and adding it to the other ones
    return _tmp_

def createHashTable(size):     # Creates the "hash table"
    _tmp_ = {}
    for num in range(size):
        _tmp_[num] = {}     # Basic initialization of a dictionary with no values
    return _tmp_

def hSearchIndex(table, pos, name):     # If a duplicate is being added to the hash table
    _tmp_ = 0                           # this function will return the amount of duplicates equally to this one

    while True:
        try:
            table[pos][str(_tmp_) + '_' + name]
            _tmp_ += 1
        except:
            break

    return _tmp_

def posValidation(table, pos, name):                    # The position is very important in a hash table
    if pos > len(table):                                # this function checks if the position calculated is within
        pos = (pos/(pos/len(table))) - ord(name[0])     # the range of the table length. This prevents any errors
    elif pos < 0:                                       # for the position.
        pos = (pos/(pos/1)) + ord(name[0])
    
    return pos

def hTableAdd(table, data):     # Adds data to the hash table
    _tmp_ = 0
    pos = round(convert2DECSum(data[0])/(3+len(str(data[0]))))     # Calcluating the position

    pos = posValidation(table, pos, data[0])    # Validate the position to prevent out of range errors.
    _tmp_ = hSearchIndex(table, pos, data[0])   # Check for the amount of duplicate names in the table

    table[pos][str(_tmp_) + '_' + data[0]] = data[1]    # Adds the data to the table
                                                        # If there is data with the same name it will add
    return table                                        # a unique ID in front of it.

def hTableGet(table, name):     # Retrieves any data from the hash table
    _tmp_ = {}

    try:
        pos = round(convert2DECSum(name)/(3+len(str(name))))   # Calculate the position of the data inside the table
                                                               
        pos = posValidation(table, pos, name)                  # Validates the position (see function: posValidation())
        nameIndex = hSearchIndex(table, pos, name)             # Counts the duplicates for the name given
    
    except:
        return "The data you are searching for doesn't exist"

    for num in range(nameIndex):
        _tmp_[str(num) + '_' + name] = table[pos][str(num) + '_' + name]    # Creates a dictionary of the search results
                                                                            # includes duplicates if there are any.
    return _tmp_

##########################
#    A little example    #
##########################

hashTable = createHashTable(500)    # Creating the "hash table"

# The example data shows a specific pattern.
# When adding data to the hash table you need to put the following properties:
#
# 0 = this one will be used as the name you can later on access the data
# 1 = is the data corresponding to the name in 0.
# ^- this data can be whatever you want it to be.

exampleData = [[{0: 'carl',1: {'age': 22, 'country': 'ch'}}], [{0: 'carl',1: {'age': 33, 'country': 'usa'}}]]

for i in range(len(exampleData)):   # looping through the data. Could be data from a .csv file
    hashTable = hTableAdd(hashTable, exampleData[i][0])     # add the data to the hash table

print(hTableGet(hashTable, 'carl'))    # example of how easy you can retrieve data with just the name
