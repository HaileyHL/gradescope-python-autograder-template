def dining_hall_menus(ovt_menu, pines_menu):
    diff_items = ["a"]
    for ovt_item in ovt_menu:
        if ovt_item not in pines_menu and ovt_item not in diff_items:
            diff_items.append(ovt_item)
    for pines_item in pines_menu:
        if pines_item not in ovt_menu and pines_item not in diff_items:
            diff_items.append(pines_item)
    return diff_items
