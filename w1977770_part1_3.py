from graphics import *
import os

def get_credit_input(prompt):
    while True:
        try:
            credit = int(input(f"Please enter your credits at {prompt}: "))
            if credit in [0, 20, 40, 60, 80, 100, 120]:
                return credit
            else:
                print('Out of range.\n')
        except ValueError:
            print('Integer required\n')

def create_graphics():
    # Grahic.py starts from top left
    # Higher Y axis - Smaller bar 
    # Lower Y axis - Taller bar
    win = GraphWin("Histogram", 400, 400)

    #Colours
    light_green = color_rgb(127,255,212)
    aquamarine3 = color_rgb(102,205,170)
    aquamarine4 = color_rgb(69,139,116)
    brown = color_rgb(165,42,42)

    # bar stats
    rect_width = 80
    x_start = 30
    y_base = 330

    progress_bar = Rectangle(Point(x_start, y_base), Point(x_start + rect_width, y_base - progress_counter * 35))
    progress_bar.setFill(light_green)
    progress_bar.draw(win)

    trailer_bar = Rectangle(Point(x_start + rect_width, y_base), Point(x_start + 2 * rect_width, y_base - trailer_counter * 35))
    trailer_bar.setFill(aquamarine3)
    trailer_bar.draw(win)

    retriever_bar = Rectangle(Point(x_start + 2 * rect_width, y_base), Point(x_start + 3 * rect_width, y_base - retriever_counter * 35))
    retriever_bar.setFill(aquamarine4)
    retriever_bar.draw(win)

    exclude_bar = Rectangle(Point(x_start + 3 * rect_width, y_base), Point(x_start + 4 * rect_width, y_base - exclude_counter * 35))
    exclude_bar.setFill(brown)
    exclude_bar.draw(win)

    # Add text labels above each bar
    progress_label = Text(Point(x_start + rect_width // 2, y_base - progress_counter * 35 - 20), str(progress_counter))
    progress_label.setSize(12)
    progress_label.setStyle("bold")
    progress_label.draw(win)

    trailer_label = Text(Point(x_start + rect_width + rect_width // 2, y_base - trailer_counter * 35 - 20), str(trailer_counter))
    trailer_label.setSize(12)
    trailer_label.setStyle("bold")
    trailer_label.draw(win)

    retriever_label = Text(Point(x_start + 2 * rect_width + rect_width // 2, y_base - retriever_counter * 35 - 20), str(retriever_counter))
    retriever_label.setSize(12)
    retriever_label.setStyle("bold")
    retriever_label.draw(win)

    exclude_label = Text(Point(x_start + 3 * rect_width + rect_width // 2, y_base - exclude_counter * 35 - 20), str(exclude_counter))
    exclude_label.setSize(12)
    exclude_label.setStyle("bold")
    exclude_label.draw(win)

    # Add labels at the bottom of each bar
    progress_bar_label = Text(Point(x_start + rect_width // 2, y_base + 10), "Progress")
    progress_bar_label.draw(win)

    trailer_bar_label = Text(Point(x_start + rect_width + rect_width // 2, y_base + 10), "Trailer")
    trailer_bar_label.draw(win)

    retriever_bar_label = Text(Point(x_start + 2 * rect_width + rect_width // 2, y_base + 10), "Retriever")
    retriever_bar_label.draw(win)

    exclude_bar_label = Text(Point(x_start + 3 * rect_width + rect_width // 2, y_base + 10), "Exclude")
    exclude_bar_label.draw(win)

    # Add label for title
    title_bar_label = Text(Point(200, 25), 'Histogram Results')
    title_bar_label.draw(win)

    # Add label for total
    total_bar_label = Text(Point(200, 375), f"{total_students} outcomes in total")
    total_bar_label.draw(win)

    if win.checkMouse() == "Close":
        win.close()

  
#Variables to act as a counter
total_students = 0
progress_counter = 0
trailer_counter = 0
retriever_counter = 0
exclude_counter = 0

   
with open('results.txt', 'w') as f:

    state = True
    
    while state:
        pass_credits = get_credit_input('pass')
        defer_credits = get_credit_input('defer')
        fail_credits = get_credit_input('fail')

        if pass_credits + defer_credits + fail_credits == 120:
            total_students +=1

            if pass_credits == 120:
                print('Progress')
                progress_counter += 1
                f.write(f"Progress - {pass_credits}, {defer_credits}, {fail_credits}\n")

            elif pass_credits == 100:
                print('Progress (module trailer)')
                trailer_counter += 1
                f.write(f"Progress (module trailer) - {pass_credits}, {defer_credits}, {fail_credits}\n")
        
            elif fail_credits >= 80:
                print('Exclude')
                exclude_counter += 1
                f.write(f"Exclude - {pass_credits}, {defer_credits}, {fail_credits}\n")

            else:
                print('Module retriever')
                retriever_counter += 1
                f.write(f"Module retriever - {pass_credits}, {defer_credits}, {fail_credits}\n")
                
        else:
            print('Total incorrect\n')
            continue

        # If user enters y, use continue to start of the while loop.
        # If user enters q, change the state variable state to false.
        while True:
            user_input= input('\nWould you like to enter another set of data?\nEnter ''y'' for yes or ''q'' to quit and view results: ')

            if user_input == 'q':
                           
                #state to break outer while loop
                state = False
                # break inner loop
                create_graphics()
                break
            elif user_input == 'y':
                # break inner loop
                break
            else:
                continue

if os.path.exists('results.txt'):
    with open('results.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            word = line.split('\n')
            print(word[0])
            
        
    
