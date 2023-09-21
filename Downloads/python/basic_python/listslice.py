#List slicing example
amazon_cart= ['samsung mobile', 'notebook', 'Grapes', 'Ball', 'Brush', 'Dishwasher', 'bodywash']
print(amazon_cart[1])
print(amazon_cart[5])
print(amazon_cart[1:3])

new_list = amazon_cart[0:3]
new_list [0]= 'gum'
print(new_list)
print(amazon_cart)

#list as Stack
stack = [1,2,3, 4, 5]
print(stack)
stack.append(6)
stack.append(7)
stack.insert(4,100)
print(stack)
new_list=stack.pop()

print(new_list)
stack.pop()
print(stack)

stack.extend([200,201])
print(stack)

#List as queue
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry") 
queue.insert(1,"Jay")   
print(queue) 
queue.append("Graham")   
print(queue)      
queue.popleft()
queue.popleft()
print(queue)      

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.sort()
print(sorted(basket))

basket.remove('Blueberries')
print(basket)
basket.append('Kiwi')
print(basket)
basket.insert(0,'Apples')
print(basket)
print(basket.count('Apples'))
print(basket.clear())

print(list(range(98)))