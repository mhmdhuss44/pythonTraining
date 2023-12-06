from queue import Queue
# first is to implement a stack using two queues:

class stack:
    def __init__(self):
        # we will use two lists as queues
        self.first=Queue()
        self.second=Queue()

    # this method is to remove and return last element in the stack  (the head)
    def stack_pop(self):
        if self.first.empty():
            return None
    #     the idea is to move all the elements to the second queue until one is remaining , we pop it
        while not self.first.empty() :
            pos = self.first.get()
            if not self.first.empty():
                self.second.put(pos)

        while not self.second.empty():
            self.first.put(self.second.get())
        return pos


    # this method is to remove to add an element to the stack:
    def stack_add(self,value):
        self.first.put(value)


#  now we will implement a queue using two stacks

class queue_mod:
    def __init__(self):
        self.first_stack=[]
        self.second_stack=[]

    def add_queue(self,value):
        self.first_stack.append(value)

    def remove_from_queue(self):
#     now this should remove the first element in the stack
        if self.first_stack is None:
            return None
        else:
            while self.first_stack:
                pos=self.first_stack.pop()
                if self.first_stack:
                    self.second_stack.append(pos)
            while self.second_stack:
                move = self.second_stack.pop()
                self.first_stack.append(move)

            return pos

# now we will write a function to check if given string of parantheses is balances
def is_balanced(given_string):
    # we will use a stack that we defined
    stack_temp=stack()
    tem_list=list(given_string)
    for value in tem_list:
        if value=='{' or value=='(' or value=='[':
            stack_temp.stack_add(value)
        else:
            popped = stack_temp.stack_pop()
            if value=='}':
                if popped=='{':
                    continue
                else:
                    return False
            if value==')':
                if popped=='(':
                    continue
                else:
                    return False
            if value==']' :
                if popped=='[':
                    continue
                else:
                    return False
    pos=stack_temp.stack_pop()
    pos = stack_temp.stack_pop()
    if pos is not None:
        return False
    return True

# easier approch from the internet
def is_balanced(given_string):
    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in given_string:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map:
            if not stack or stack.pop() != parentheses_map[char]:
                return False

    return not stack


if __name__ == '__main__':
            first_stack=stack()
            first_stack.stack_add(6)
            first_stack.stack_add(7)
            first_stack.stack_add(8)
            first_stack.stack_add(25)
            popped=first_stack.stack_pop()
            print("the removed element or last inserted is:",popped)
            print("the second removed element is:", first_stack.stack_pop())

            try_queue=queue_mod()
            try_queue.add_queue(5)
            try_queue.add_queue(20)
            try_queue.add_queue(7)
            try_queue.add_queue(14)
            removed=try_queue.remove_from_queue()
            print("the removed element is ",removed)
            print("the second removed element is ", try_queue.remove_from_queue())

            pos="(([()]))"
            print("the result is",is_balanced(pos))

