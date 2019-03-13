#!/usr/bin/env python
# coding: utf-8

# In[130]:


from TreeNode import Tree
from TreeNode import Node
import random
import queue
from LinkedList import LinkedNode
from LinkedList import LinkedList
from Plotter import Plotter
import timeit


# In[131]:


class Runner:
    
    def __init__(self, DATA_SIZE, DATA_RANGE):
        self.DATA_SIZE = DATA_SIZE
        self.DATA_RANGE = DATA_RANGE
        self.data =  random.sample(range(0, DATA_RANGE), DATA_SIZE)
        self.data_list = []
        self.data_tree = Tree()
        self.data_set = set()
        self.data_dict = {}
        self.data_linked_list = LinkedList()
        
        
    def list_search(self, data_list, target):
        for i in range(len(data_list)):
                if data_list[i] == target:
                    break
        
        
    def runner_controller(self, data_structure, name, num, operation):
        if(name == "list"):
            if(operation == "format"):
                data_structure.append(num)
            elif(operation == "search"):
                self.list_search(data_structure, num)
            elif(operation == "delete"):
                temp_data_structure = data_structure
                temp_data_structure.remove(num)
            else:
                print("Unknow Operation Name: " + operation)
            
        elif(name == "tree"):
            if(operation == "format"):
                data_structure.insert(num)
            elif(operation == "search"):
                data_structure.search(num)
            elif(operation == "delete"):
                temp_data_structure = data_structure
                temp_data_structure.delete(num)
            else:
                print("Unknow Operation Name: " + operation)
                
        elif(name == "set"):
            if(operation == "format"):
                data_structure.add(num)
            elif(operation == "search"):
                num in data_structure
            elif(operation == "delete"):
                temp_data_structure = data_structure
                temp_data_structure.remove(num)
            else:
                print("Unknow Operation Name: " + operation)
                
        elif(name == "dictionary"):
            if(operation == "format"):
                data_structure[num] = num
            elif(operation == "search"):
                if num in data_structure:
                    pass
            elif(operation == "delete"):
                temp_data_structure = data_structure
                del temp_data_structure[num]
            else:
                print("Unknow Operation Name: " + operation)
                
        elif(name == "linked_list"):
            if(operation == "format"):
                data_structure. addNode(num)
            elif(operation == "search"):
                data_structure.search(num)
            elif(operation == "delete"):
                temp_data_structure = data_structure
                temp_data_structure.remove(num)
            else:
                print("Unknow Operation Name: " + operation)
                
        else:
            print ("Wrong Structure Name Parsed:  " + name)
            
            
            
    def formmer(self, name, FORM_LOOP_TIME, data_structure):
        count_time = 0
        for count in range(FORM_LOOP_TIME):
            start_time = timeit.default_timer()
            for num in self.data:
                self.runner_controller(data_structure, name, num, "format")
            count_time += timeit.default_timer() - start_time
        form_time = round(count_time / FORM_LOOP_TIME, 4)
        return data_structure, form_time
        
        
        
        
    def formate_data(self, FORM_LOOP_TIME):
        self.data_list, list_form_time = self.formmer("list", FORM_LOOP_TIME, self.data_list)
        self.data_tree, tree_form_time = self.formmer("tree", FORM_LOOP_TIME, self.data_tree)
        self.data_set, set_form_time = self.formmer("set", FORM_LOOP_TIME, self.data_set)
        self.data_dict, dict_form_time = self.formmer("dictionary", FORM_LOOP_TIME, self.data_dict)
        self.data_linked_list, linked_list_form_time = self.formmer("linked_list", FORM_LOOP_TIME, self.data_linked_list)
        
        return self.data_list, list_form_time, self.data_tree, tree_form_time, self.data_set, set_form_time, self.data_dict, dict_form_time, self.data_linked_list, linked_list_form_time
        
    
    def search(self, name, SEARCH_LOOP_TIME, targets, data_structure):
        count_time = 0
        for target in targets:
            start_time = timeit.default_timer()
            self.runner_controller(data_structure, name, target, "search")
            count_time += round((timeit.default_timer() - start_time) * 1000)
                 
        search_time = count_time / SEARCH_LOOP_TIME 
        return search_time
        
        
    def delete(self, name, DELETE_LOOP_TIME, targets, data_structure):
        count_time = 0
        for target in targets:
            start_time = timeit.default_timer()
            self.runner_controller(data_structure, name, target, "delete")
            count_time += round((timeit.default_timer() - start_time) * 1000)
                 
        delete_time = count_time / DELETE_LOOP_TIME 
        return delete_time
        

