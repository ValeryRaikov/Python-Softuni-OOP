def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"
            
        return wrapper
    
    return decorator


@tags('p')
@tags('b')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
