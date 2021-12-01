class Node :
    def __init__ ( self, data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
        
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
    
    def reverse ( self ) :
        prev = None
        current = self.head
        while ( current is not None ) :
            next_one = current.next
            current.next = prev
            prev = current
            current = next_one
        self.head = prev
    
    def sortedMerge ( self, a, b ) :
        result = None
        if a == None : return b
        if b == None : return a
             
        if a.data <= b.data :
            result = a
            result.next = self.sortedMerge ( a.next, b )
        else :
            result = b
            result.next = self.sortedMerge ( a, b.next )
        return result
     
    def mergeSort ( self, h ) :
        if ( h == None or h.next == None ) : return h
 
        middle = self.getMiddle ( h )
        next_to_middle = middle.next
        middle.next = None

        left = self.mergeSort ( h )
        right = self.mergeSort ( next_to_middle )
        
        sorted_list = self.sortedMerge(left, right)
        return sorted_list
        
    def getMiddle ( self, head ) :
        if ( head == None ) : return head

        slow = head
        fast = head
        while ( fast.next != None and fast.next.next != None ) :
            slow = slow.next
            fast = fast.next.next
        return slow

llist = LinkedList()
llist.head = Node ( 1 )
llist.head.next = Node ( 2 )
llist.head.next.next = Node ( 3 )
llist.reverse()
llist.printList()
llist.head = llist.mergeSort( llist.head )
llist.printList()