
# in the file we will solve some linked list questions

# first we will define our classes
class node:
    def __init__(self,value):
        self.value=value
        self.next= None

class linkedList:

    def __init__(self):
        self.head=None

    def printlist(self):
        pos = self.head
        #     now we will loop to the end of list
        while pos is not None:
            print(pos.value)
            pos = pos.next



    def add_last(self,node):
        if self.head is None:
            self.head=node
        else :
            pos=self.head
        #     now we will loop to the end of list
            while pos.next is not None:
                pos=pos.next
            pos.next=node




# a function to print a linked list
def print_list(arr):
    pos = arr
    #     now we will loop to the end of list
    while pos is not None:
        print(pos.value)
        pos = pos.next


# a funtion to reverse a linked list
def reverse_list(temp_list):
        first = temp_list.head
        second = None
        while first is not None:
            pos = first.next
            first.next = second
            second = first
            first = pos
        temp_list.head = second
        return temp_list.head

# additional function to print a linked list using recursion
def rec_reverse(temp_list):
    if temp_list.next is None or temp_list is None:
        return temp_list
    head=rec_reverse(temp_list.next)
    # reverse the link between the current node and the next node
    temp_list.next.next = temp_list
    temp_list.next = None
    return head

# a function to  find the middle eleement in linked list
# note: this will ruine the original list

def middle_element(temp_list):
    first=temp_list.head
    second=temp_list.head

    while second.next is not None and second.next.next is not None:
        first=first.next
        second=second.next.next

    return first

def check_cycle(temp_list):
    first = temp_list.head
    second = temp_list.head.next
    if not first or not first.next:
        return False
    while first != second :
        if second is None or second.next is None  :
            return False
        first=first.next
        second=second.next.next
    return True



if __name__ == '__main__':
    mylist=linkedList()
    mylist.add_last(node(5))
    mylist.add_last(node(8))
    mylist.add_last(node(5))
    mylist.add_last(node(54))
    mylist.printlist()

    # ******************************* questions 1 ******************************
    # # reverse list check
    # arr=reverse_list(mylist)
    # print("the reversed lined list : ")
    # print_list(arr)

    # reversed list using recursion
    # print("the reversed lined list using recursion : ")
    # second_list=rec_reverse(arr)
    # print_list(second_list)

    # ******************************* questions 2 ******************************

    # # printing the mid value of the list
    # print("the mid value is")
    # middle=middle_element(mylist)
    # print(middle.value)

    # ******************************* questions 3 ******************************

    # a piece of code that adds a cycle to a list
    # pos = mylist.head
    # start=mylist.head.next
    # #     now we will loop to the end of list
    # while pos.next is not None:
    #     pos = pos.next
    # pos.next=start
#     prining yes/no if the list have a cycle or not
#     flag=check_cycle(mylist)
#     print("does the list have a cycle? ",flag)








