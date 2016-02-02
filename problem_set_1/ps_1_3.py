def item_order(order):
    salad_count, hamburger_count, water_count = 0, 0, 0
    
    order_list = order.split(' ')
    
    for order in order_list:
        if order == 'salad':
            salad_count += 1
        elif order == 'hamburger':
            hamburger_count += 1
        elif order == 'water':
            water_count += 1
            
    return 'salad:%d hamburger:%d water:%d' % (salad_count, hamburger_count, water_count)