# Teplova
calls = 0
def count_calls():
    global calls
    calls  = calls + 1 # changing the meaning of the "calls" (calls += 1)
def string_info(string):
    count_calls() # count the function here!
    return(len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):
    count_calls()
    string = string.lower()
    for str in list_to_search:
        if str.lower() == string:
            return True
    return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(string_info('YTRjjsjsjsjsj'))
print(string_info('ewpakdyfnsks,cdhsh'))
print(is_contains('Oryshayk', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('ujty', ['recycling', 'cyclic']))
print(calls)
