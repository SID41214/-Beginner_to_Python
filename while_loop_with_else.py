fruits =['apple','banana','mango','strawberry']
fruits_len =len(fruits)
index =0
# fruit_found =False
while index < fruits_len:
    if fruits[index] == 'orange':
        # fruit_found =True
        print('orange is available')
        break
    index += 1
# if not fruit_found:
else:
    print("orange is not available")