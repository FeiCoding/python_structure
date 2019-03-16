from Runner import *
from Plotter import *

NAME = ['List', 'Sorted List', 'Tree', 'Set', 'Dictionary', 'Linked List']
DATA_SIZE = 100000000
DATA_RANGE = 100000000
runner = Runner(DATA_SIZE, DATA_RANGE)


def plot_graph(time, operation_name):
    plot = Plotter()
    plot.diagram_plot(time, NAME, operation_name)


def data_search(search_loop_time, data_list, data_tree, data_set, data_dict, data_linked_list, data_sort_list):
    targets = [random.randint(0, DATA_SIZE) for i in range(search_loop_time)]
    print(targets)
    list_search_time = runner.search("list", search_loop_time, targets, data_list)
    sorted_list_search_time = runner.search("sort_list", search_loop_time, targets, data_sort_list)
    tree_search_time = runner.search("tree", search_loop_time, targets, data_tree)
    set_search_time = runner.search("set", search_loop_time, targets, data_set)
    dict_search_time = runner.search("dictionary", search_loop_time, targets, data_dict)
    linked_list_search_time = runner.search("linked_list", search_loop_time, targets, data_linked_list)
    time_search = [list_search_time, sorted_list_search_time, tree_search_time, set_search_time, dict_search_time, linked_list_search_time]
    plot_graph(time_search, "Search Time")


def data_delete(delete_loop_time, data_list, data_tree, data_set, data_dict, data_linked_list, data_sort_list):
    targets = [random.randint(0, DATA_SIZE) for i in range(delete_loop_time)]
    list_delete_time = runner.delete("list", delete_loop_time, targets, data_list)
    sort_list_delete_time = runner.delete("sort_list", delete_loop_time, targets, data_sort_list)
    tree_delete_time = runner.delete("tree", delete_loop_time, targets, data_tree)
    set_delete_time = runner.delete("set", delete_loop_time, targets, data_set)
    dict_delete_time = runner.delete("dictionary", delete_loop_time, targets, data_dict)
    linked_list_delete_time = runner.delete("linked_list", delete_loop_time, targets, data_linked_list)
    time_delete = [list_delete_time, sort_list_delete_time, tree_delete_time, set_delete_time, dict_delete_time, linked_list_delete_time]
    plot_graph(time_delete, "Delete Time")


def data_runner():
    data_list, list_form_time, data_tree, tree_form_time, data_set, set_form_time, data_dict, dict_form_time, data_linked_list, linked_list_form_time, data_sort_list, sort_list_form_time = runner.format_data()
    time_insert = [list_form_time, sort_list_form_time, tree_form_time, dict_form_time, dict_form_time, linked_list_form_time]
    plot_graph(time_insert, "Forming Time")
    return data_list, data_tree, data_set, data_dict, data_linked_list, data_sort_list

def main():
    data_list, data_tree, data_set, data_dict, data_linked_list, data_sort_list = data_runner()
    data_search(10, data_list, data_tree, data_set, data_dict, data_linked_list, data_sort_list)
    data_delete(10, data_list, data_tree, data_set, data_dict, data_linked_list, data_sort_list)


if __name__ == "__main__":
        main()
