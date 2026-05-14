"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for item in items_to_add:
        if current_cart.get(item,False):
            current_cart[item]+=1
        else:
            current_cart[item]=1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    return dict.fromkeys(notes,1) 


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    ideas |= recipe_updates
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    Parameters:
        cart (dict): A users shopping cart dictionary.

    Returns:
        dict: A sers shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    Parameters:
        cart (dict): The users shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    
    for item,quantity in sorted(cart.items(),reverse=True):
        fulfillment_cart[item]=[quantity]+aisle_mapping[item]
        
    return fulfillment_cart
        


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    for item,details in fulfillment_cart.items():
        if store_inventory[item][0] != "Out of Stock":
            store_inventory[item][0]-=details[0]
            if store_inventory[item][0]<=0:
                store_inventory[item][0]="Out of Stock"
    return store_inventory
