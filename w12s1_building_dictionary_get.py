def our_get(d, key, default=None):
    # return the value tied to the key if the key is valid
    # return None otherwise
    # You are not allowed to raise an error here

    try:
        return d[key]
    except:
        return default

attendance = {'Taiwo':'Late'}
result = our_get(attendance, 'Salmane', 'Absent')
print(result)