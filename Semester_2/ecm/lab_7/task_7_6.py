class EmptyLinkedList(Exception):
    ...
    
class LastElementInArray(Exception):
    ...

class Item:
    #class constructor
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
        
    #Initializing all getters and setters
    def get_data(self) -> object:
        return self.data
    
    def set_data(self, data: object):
        self.data = data
        
    def get_next(self) -> object:
        return self.next
    
    def set_next(self, next: object):
        self.next = next
        
    def get_prev(self) -> object:
        return self.prev
    
    def set_prev(self, prev: object):
        self.prev = prev

    def remove(self) -> None:
        if self.next != None:
            self.next.set_prev(self.prev)
            self.prev.set_next(self.next)
        else:
            raise LastElementInArray

class MyList:
    def __init__(self, head: object = Item(None, None, None)):
        self.head = head
        self.tail = head

    def get_tail(self):
        return self.tail
    
    def get_head(self):
        return self.head

    # метод добавления элемента в конец списка
    def append(self, x: object) -> None:
        
        #Create a new Item obj
        itemToAppend = Item(x, prev = self.tail)
        
        #if we have nothing in our list we just make an object
        if self.head.get_next() == None:
            self.head.set_next(itemToAppend)
            self.tail = itemToAppend
            self.tail.set_prev(self.head)
        #if we have something, we set our new item as next and bring our tail to it, to create a link(connection)
        else:
            self.tail.set_next(itemToAppend)
            self.tail = itemToAppend

    # метод удаления элемента из конца списка (не забываем про пустой список!)
    def pop(self) -> object:
        #if list isEmpty then we raise Exception
        if self.head.get_next() == None:
            raise EmptyLinkedList
        
        #else we just copy data to return it and move our tail to prev location
        else:
            data = self.tail.get_data()
            prev = self.tail.get_prev()
            
            prev.set_next(None)
            self.tail = prev
            
            return data
        
    # метод добавления элемента в начало списка (помним про указатель tail!)
    def pushFirst(self, x: object) -> None:
        itemToAppend = Item(x, self.head.get_next(), self.head)
        
        if self.head.get_next() == None:
            self.tail = itemToAppend
        else:
            prevHeadNext = self.head.get_next()
            prevHeadNext.set_prev(itemToAppend)
        
        self.head.set_next(itemToAppend)
        
    # метод удаления элемента из начала списка (опять не забываем про пустой список!)
    def popFirst(self):
        if self.head.get_next() == None:
            raise EmptyLinkedList
        
        item = self.head.get_next()
        data = item.get_data()
        
        if item.get_next() != None:
            item.remove()
        else:
            self.tail = self.head
            self.head.set_next(None)
            
        return data

    # метод определения длины списка
    def __len__(self):
        cnt = 0
        item = self.head
        
        while item.get_next() != None:
            cnt += 1
            item = item.get_next()
            
        return cnt

    # метод конструирования строкового представления списка
    def __str__(self):
        retString = ""
        item = self.head.get_next()
        while item != None:
            retString += str(item.get_data())
            if item.get_next() != None:
                retString += ", "
            item = item.get_next()
            
        return f"[{retString}]"

A = MyList()
A.append(1)
A.pushFirst(3)
A.append(5)
A.append(1)
A.pushFirst(5)
print(A)
print(A.popFirst())
print(A.pop())
print(A)
print(len(A))
