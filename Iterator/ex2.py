value='good'
iter_value=iter(value)
while True:
    try:
        item =next(iter_value)
        print(item)
    except StopIteration:
        break