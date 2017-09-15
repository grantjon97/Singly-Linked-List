# singly_linked_list.py
# Jonathan Grant - 04/30/2016
# Implements a singly linked list by reading a text file.

class List_node():
    """ Creates a node with a name and amount. """

    # self.name - the word that will be inserted to the node
    # self.amount - number of times the word comes up
    # self.next - points to the next node in the list

    def __init__(self, name):
        """ Initializes the node. """

        self.name = name
        self.amount = 1
        self.next = None

    def print(self):
        """ Prints the node and its frequency. """

        print(self.name, ': ', self.amount, sep = '')

class My_list():
    """ Contains the methods of a singly linked list.

    Methods include:

    Searching for a certain word
    Inserting a new word
    Deleting a word
    Printing the list itself
    """

    def __init__(self):
        """ Initializes an empty singly-linked list. """

        # self.head - Points to the first item in the list

        self.head = None

    def check_for_node(self, name):
        """ Searches for a specific node, says if it exists.

        name - the name of the node being searched for

        Returns a boolean - True if node exists, false if not.
        """

        # done - Boolean stating whether we need to keep
        #        traversing the list or not
        # p - points to the current node being looked at
        # node_exists - Boolean stating if the node searched
        #               for exists

        p = self.head
        done = False
        node_exists = False

        # Keep traversing until the node is found,
        # or until the end of the list is reached.
        while (not done):

            # If the list is empty, the node
            # does not exist.
            if (p is None):

                done = True

            # Compare the name entered with the name of
            # each node.
            else:

                if p.name == name:

                    node_exists = True
                    done = True

                else:

                    p = p.next

        return node_exists

    def traverse(self):
        """ Prints the list and number of words in the list. """

        # number_of_total_words - Number of words including repeats
        # number_of_processed_words - Number of different words.

        number_of_total_words = 0
        number_of_processed_words = 0
        p = self.head

        while p:

            p.print()
            number_of_total_words += p.amount
            number_of_processed_words += 1
            p = p.next

        print('\nNumber of total words:', number_of_total_words)
        print('\nNumber of words stored in list: ', end='')
        print(number_of_processed_words)
        print()

    def delete_node(self, name):
        """ Deletes a node.

        Deletes the node based off of a given name.
        """


        done = False
        p = self.head
        q = None

        # Keep traversing until the node is found, or
        # if it is found that the node already does not exist.
        while (not done):

            # If p is None, it must be an empty list, or
            # p may have gone through the entire list, without
            # finding the desired node.
            if (p is None):

                print('The word', name, 'does not exist.')
                done = True

            elif (name == p.name):

                # Delete the node at the beginning of the list,
                # or if it's the only node in the list.
                if (q is None):

                    self.head = p.next
                    done = True

                # Delete a middle or last node in the list.
                else:

                    q.next = p.next
                    done = True

            # Move p and q forward when the node pointed to is not
            # the correct node to delete.
            else:

                q = p
                p = p.next


    def insert_node(self, name):
        """ Inserts a node into alphabetical order.

        Note: If the node already exists, the node's
              amount is incremented instead.
        """

        done = False
        p = self.head
        q = None

        # Keep traversing until the correct location to
        # insert the node is found and inserted.
        while (not done):

            # Insert into an empty list
            if (self.head is None):

                self.head = List_node(name)
                done = True

            elif (p is not None) and (name < p.name):

                # Insert a node at middle of list
                if q:

                    temp = List_node(name)
                    temp.next = p
                    q.next = temp
                    done = True

                # Insert at node at the beginning of list
                else:

                    temp = List_node(name)
                    temp.next = p
                    self.head = temp
                    done = True

            # Increment the node's amount if it already exists.
            elif (p is not None) and (name == p.name):

                p.amount = p.amount + 1
                done = True

            # Insert a node at the end of the list.
            elif q and (not p):

                q.next = List_node(name)
                done = True

            # Move p and q forward if the correct location
            # is not found.
            else:

                q = p
                p = p.next

def process_file():
    """ Translates the words from a .txt into a singly linked list.

    Requires the user to input a filename, then
    puts the words into a singly linked list.

    Deletes small stop words, and then shows the new list.
    """

    # text_file_list - The singly linked list
    # file_name - name of the .txt file the user inputs
    # f - Name given to open the filename


    text_file_list = My_list()
    file_name = input('What is the name of the file? ')

    # Open the .txt file and insert its words into the list

    f = open(file_name)

    for line in f:

        for word in line.split():

            text_file_list.insert_node(word)

    f.close()

    # Print the list, with and then without stop words.

    print('\nList with stop words:\n')
    text_file_list.traverse()

    # Delete all stop words in the list.
    for word in ['a', 'an', 'the']:

        text_file_list.delete_node(word)

    print('\nList without stop words:\n')
    text_file_list.traverse()

def display_program_info():
    """ Displays information on the program functionality. """

    print()
    print('singly_linked_list.py')
    print('This program implements the methods of a singly')
    print('linked list. A text file is read, and individual')
    print('words are inserted into the list in alphabetical')
    print('order. They are displayed, along with how many')
    print('times they show up in the text file in this format:')
    print()
    print('word: number of occurences')
    print()

def Main():
    """ Implements a singly linked list from a text file. """

    display_program_info()

    process_file()

Main()
