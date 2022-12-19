#To list the color from comma separated and display the first and last colour
color=input("Enter the color:")
print(color)
color_list=color.split(',')
print(color_list)
print("The first color is ",color_list[0])
print("The last color is ",color_list[3])