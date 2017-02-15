shopping_list = {
    "target": ["socks", "soap", "detergent", "sponges"],
    "bi-rite": ["butter","cake","cookies","bread"],
    "berkeley_bowl": ["apples","oranges","bananas","milk"],
    "safeway": ["oreos","brownies","soda"],
}


main_menu = """0 Main Menu
1 Show all lists.
2 Show a specific list.
3 Add a new shopping list.
4 Add an item to a shopping list.
5 Remove an item from a shopping list.
6 Remove a list by nickname.
7 Exit when you are done."""

print main_menu

def add_new_shopping_list(new_store):
    shopping_list[new_store] = []
    print shopping_list
    return shopping_list

def check_store_exists(store_name):
    if store_name in shopping_list:
        return True
    else:
        return False

def check_item_exists(item):
    if item in shopping_list:
        return True
    else:
        return False

def add_item_to_store_list(store_name, item):
    shopping_list[store_name].append(item)
    print shopping_list
    return shopping_list

def remove_item_from_store_list(store_name, item):
    shopping_list[store_name].remove(item)
    print shopping_list
    return shopping_list

def remove_store(store_name):
    del shopping_list[store_name]
    print shopping_list
    return shopping_list
def parse_input_string(input_string):
def main():
    user_choice = int(raw_input("Please select a number from the menu "))
    if user_choice == 0:
        print main_menu
    if user_choice == 1:
        print shopping_list
    if user_choice == 2:
        specific_list = raw_input("Which list would you like to access? ").lower()
        print shopping_list[specific_list]
    if user_choice == 3:
        new_list_name = raw_input("What do you want to call your new shopping list? ").lower()
        if new_list_name in shopping_list:
            print "That's already there. "
        else:
            shopping_list[new_list_name] = []
    if user_choice == 4:
        store_name = raw_input("What store do you want to add an item to? ").lower()
        if check_store_exists(store_name):
            add_item = raw_input("What item would you like to add? ").lower()
            if not check_item_exists(add_item):
                add_item_to_store_list(store_name, add_item)
            else:
                print "The item doesn't exist. "
    if user_choice == 5:
        store_name = raw_input("What store do you want to remove an item from? ").lower()
        if check_store_exists(store_name):
            remove_item = raw_input("What item would you like to remove? ").lower()
            if check_item_exists(remove_item):
                remove_item_from_store_list(store_name)
            else:
                print "The item doesn't exist. "
    if user_choice == 6:
        store_name = raw_input("What store list would you like to remove? ")
        if check_store_exists(store_name):
            remove_store(store_name)
        else: 

            print "That store doesn't exist. "






if __name__ == '__main__':
    main()
