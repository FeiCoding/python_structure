
# coding: utf-8

# In[1]:

from TreeNode import Tree
import random
from LinkedList import LinkedList
import timeit
from sortedcontainers import SortedList


# In[2]:

class Runner:
    
    def __init__(self, data_size, data_range):
        self.DATA_SIZE = data_size
        self.DATA_RANGE = data_range
        self.data = random.sample(range(0, data_range), data_size)
        self.data_list = []
        self.data_tree = Tree()
        self.data_set = set()
        self.data_dict = {}
        self.data_linked_list = LinkedList()
        self.data_sort_list = SortedList()
        
    def list_search(self, data_list, target):
        for num in data_list:
                if num == target:
                    break

    def runner_controller(self, data_structure, name, num, operation):
        if name == "list":
            if operation == "format":
                data_structure.append(num)
            elif operation == "search":
                self.list_search(data_structure, num)
            elif operation == "delete":

                temp_data_structure = data_structure
                try:
                    temp_data_structure.remove(num)
                except:
                    print("The target is " + str(num))
                    print(len(data_structure))
                    for n in data_structure:
                        print("The content is " + str(n))
            else:
                print("Unknown Operation Name: " + operation)
            
        elif name == "tree":
            if operation == "format":
                data_structure.insert(num)
            elif operation == "search":
                data_structure.search(num)
            elif operation == "delete":
                temp_data_structure = data_structure
                temp_data_structure.delete(num)
            else:
                print("Unknown Operation Name: " + operation)
                
        elif name == "set":
            if operation == "format":
                data_structure.add(num)
            elif operation == "search":
                num in data_structure
            elif operation == "delete":
                temp_data_structure = data_structure
                temp_data_structure.remove(num)
            else:
                print("Unknown Operation Name: " + operation)
                
        elif name == "dictionary":
            if operation == "format":
                data_structure[num] = num
            elif operation == "search":
                if num in data_structure:
                    pass
            elif operation == "delete":
                temp_data_structure = data_structure
                del temp_data_structure[num]
            else:
                print("Unknown Operation Name: " + operation)
                
        elif name == "linked_list":
            if operation == "format":
                data_structure. addNode(num)
            elif operation == "search":
                data_structure.search(num)
            elif operation == "delete":
                temp_data_structure = data_structure
                temp_data_structure.remove(num)
            else:
                print("Unknown Operation Name: " + operation)
        
        elif name == "sort_list":
            if operation == "format":
                data_structure.add(num)
            elif operation == "search":
                data_structure.index(num)
            elif operation == "delete":
                temp_data_structure = data_structure
                temp_data_structure.remove(num)
            else:
                print("Unknown Operation Name: " + operation)
        else:
            print ("Wrong Structure Name Parsed:  " + name)

    def former(self, name, data_structure):
        start_time = timeit.default_timer()
        for num in self.data:
            self.runner_controller(data_structure, name, num, "format")
        form_time = timeit.default_timer() - start_time
        form_time = round(form_time * 1000, 3)
        return data_structure, form_time
        
    def format_data(self):
        self.data_list, list_form_time = self.former("list", self.data_list)
        self.data_tree, tree_form_time = self.former("tree", self.data_tree)
        self.data_set, set_form_time = self.former("set", self.data_set)
        self.data_dict, dict_form_time = self.former("dictionary", self.data_dict)
        self.data_linked_list, linked_list_form_time = self.former("linked_list", self.data_linked_list)
        self.data_sort_list, sort_list_form_time = self.former("sort_list", self.data_sort_list)
        return self.data_list, list_form_time, self.data_tree, tree_form_time, self.data_set, set_form_time, self.data_dict, dict_form_time, self.data_linked_list, linked_list_form_time, self.data_sort_list, sort_list_form_time

    def search(self, name, loop_time, targets, data_structure):
        count_time = 0
        for target in targets:
            start_time = timeit.default_timer()
            self.runner_controller(data_structure, name, self.data[target], "search")
            count_time += round((timeit.default_timer() - start_time) * 1000)
                 
        search_time = count_time / loop_time
        return search_time

    def delete(self, name, loop_time, targets, data_structure):
        count_time = 0
        for target in targets:
            start_time = timeit.default_timer()
            self.runner_controller(data_structure, name, self.data[target], "delete")
            count_time += round((timeit.default_timer() - start_time) * 1000)
                 
        delete_time = count_time / loop_time
        return delete_time

