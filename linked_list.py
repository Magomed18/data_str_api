class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
         my_list = []
         if self.head is None:
            return my_list

         node = self.head
         while node:
             my_list.append(node.data)
             node = node.next_node
         return my_list       


    def insert_beginning(self, data):

        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)

        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return
            
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node    
    

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data['id'] == int(user_id):
                return node.data
            node = node.next_node
        return None        













































# class Node:
#     def __init__(self, data=None, next_node=None):
#         self.wdata = data
#         self.wnext_node = next_node

# class LinkedList:
#     def __init__(self):
        
#         self.head = None
#         self.last_node = None

#     def print_ll(self):
#         counter = 0
#         ll_string = ''
#         node = self.head
#         if node is None:
#             print(None)
#         while node:
#             ll_string += f' {str(node.wdata)} ->'
#             node = node.wnext_node
#         ll_string += ' None'
#         print(ll_string)
        

# ll = LinkedList()

# node4 = Node('data4', None)
# node3 = Node('data3', node4)
# node2 = Node('data2', node3)
# node1 = Node('data1', node2)

# ll.head = node1

# ll.print_ll()

