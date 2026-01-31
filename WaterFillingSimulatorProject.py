

def print_glass(height, width, water):

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if water > (glass_height * glass_width):

        new_water = (water - (glass_width*glass_height))

        the_column_should_fill = int(new_water/glass_height)

        the_column_fill_by_parts = (new_water%glass_height)

        for i in range((glass_height+2)):

            if i <= (glass_height-1):

                if the_column_fill_by_parts >= (glass_height - i):
                    print("|" + "*" * glass_width + "|" + "*" * the_column_should_fill + "*")
                else:
                    print("|" + "*" * glass_width + "|" + "*" * the_column_should_fill)



            elif i == glass_height:
                if the_column_fill_by_parts > (glass_height - i):
                    print("-" * (glass_width+2) + "^" * the_column_should_fill + "^")
                else:
                    print("-" * (glass_width+2) + "^" * the_column_should_fill)
            else:
                if the_column_fill_by_parts > (glass_height - (i-1)):
                    print("#" * (glass_width+2) + "#" * the_column_should_fill + "#")
                else:
                    print("#" * (glass_width+2) + "#" * the_column_should_fill)





    else:


        for i in range((glass_height+2)):
            if i <= (glass_height-1):
                if i >= (glass_height - int(water/glass_width)):
                    print("|" + "*" * glass_width + "|")
                elif i == glass_height - int((water/glass_width)+1):
                    print("|" + "*" * (water%glass_width) + " " * (glass_width-(water%glass_width)) + "|")
                else:
                    print("|" + " " * glass_width + "|")
            elif i == glass_height:
                print("-" * (glass_width + 2))
            else:
                print("#" * (glass_width + 2))
    print()
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

water = 0

glass_width = int(input())
glass_height = int(input())
fill_count = int(input())

for _ in range(fill_count):
    water = water + int(input())
    print_glass(glass_height, glass_width, water)

