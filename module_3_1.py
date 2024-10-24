calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    return len(string), str(string).upper(), str(string).lower()

def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        if string.casefold() == item.casefold():
            return True
    else:
            return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
