'''
Exercise 8:Widgets and Gizmos
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
'''

widgets_no  = float(input('How many widget(s) did you order? '))
gizmo_no  = float(input('How many gizmo(s) did you order? '))


widgets = 75
gizmo = 112

total = widgets * widgets_no + gizmo * gizmo_no

print('The total weight of your order is {}'.format(total))