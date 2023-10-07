def vowel_filter(function):
    VOWELS = ['a', 'o', 'u', 'e', 'i', 'y']
    
    def wrapper():
        return [char for char in function() if char in VOWELS]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
