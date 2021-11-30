# Create Node class

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


# Create LinkedList class with mergeSort method

class LinkedList():

    def __init__(self):
        self.head = None

    def append(self, new_value):
        ''' Append method to add new values to the list. '''
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head

        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = new_node

    def getMiddle(self, head):
        ''' Utility function to get the middle of a linked list.'''
        if head == None:
            return head

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeSort(self, h):
        '''
            Merge sort linked list.
        '''
        # base case if head is None
        if h == None or h.next == None:
            return h

        # get the middle of the list
        middle = self.getMiddle(h)
        next_to_middle = middle.next

        middle.next = None

        # apply mergeSort on left lists
        left = self.mergeSort(h)
        # apply mergeSort on right lists
        right = self.mergeSort(next_to_middle)

        # merge the left and right lists
        sorted_list = self.sortedMerge(left, right)

        return sorted_list

    def sortedMerge(self, a, b):
        result = None

        if a == None:
            return b
        if b == None:
            return a

        # pick either a or b with smaller value
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)

        return result

    def reverse(self):
        '''
            Reverse linked list.
        '''
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
            
            
# utility function to print values of a linked list
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end = ' -> ')
        curr_node = curr_node.next
    print('None')


if __name__ == '__main__':

    ll = LinkedList()
    ll.append(2)
    ll.append(-5)
    ll.append(10)
    ll.append(22)
    ll.append(0)
    ll.append(7)
    ll.append(-3)
    
    print ("Linked List is:")
    printList(ll.head)

    print('Middle Node data is:')
    print(ll.getMiddle(ll.head).data)

    print ("Sorted Linked List is:")
    ll.head = ll.mergeSort(ll.head)
    printList(ll.head)

    print()
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(-5)

    
    print ("Linked List is:")
    printList(ll2.head)

    print('Middle Node data is:')
    print(ll2.getMiddle(ll2.head).data)

    print ("Sorted Linked List is:")
    ll2.head = ll2.mergeSort(ll2.head)
    printList(ll2.head)

    print('\n Reversing linked list')
    ll = LinkedList()
    ll.append(2)
    ll.append(-5)
    ll.append(10)
    ll.append(22)
    ll.append(0)
    ll.append(7)
    ll.append(-3)
    
    print ("Linked List is:")
    printList(ll.head)

    ll.reverse()
    print ("Reversed Linked List is:")
    printList(ll.head)

    print ("Sorted Linked List is:")
    ll.head = ll2.mergeSort(ll.head)
    printList(ll.head)

    print ("Reverse sorted Linked List is:")
    ll.reverse()
    printList(ll.head)
