def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string),string.upper(),string.lower()

def is_contains(string, list_to_search):
    count_calls()
    new_string = string.upper()
    new_li = [x.upper() for x in list_to_search]
    return new_string in new_li


calls = 0



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)