"""

This program allows users to create, list, update, and delete tasks within the CLI.

Created by Ivan Mann
Date: 05-28-2026

"""

import time
import json
import sys


task_list = []



def create_id():
        number = 0
        def id():
            nonlocal number
            number += 1
            return number
        return id
id = create_id()

def create_task():
    task = {
        'ID':'',
        'Task': '',
        'Status': '',
        'Time Created': '',
        'Time Updated': ''
    }
    
    current_id = id()
    task['ID'] = current_id

    try:
        desc = str(input("\nEnter Task ([0] for Main Menu ): "))
        stat = str(input("Enter Status ('todo', 'in-progress', 'done'): "))
        if desc == '0':
            task_manager()
        else:

            time_cre = time.strftime("%a, %d %b %Y %I:%M:%S")

            print(f"\nTask added succesfully. Time: {time_cre}")

            task['Status'] = stat
            task['Task'] = desc
            task['Time Created'] = time_cre
            task_list.append(task)
            task_manager()
            

    except ValueError:
        print("Error: Please try again.")

    
    
    

def delete_task():
    
    j = input("ID # ([0] for Main Menu) : ")
    if j == '0':
        task_manager()
    elif j >= '1':
        for i in range(len(task_list)):
            if task_list[i]['ID'] == int(j):
                del task_list[i]
                break

        print(json.dumps(task_list, indent=4))
        print("Task Deleted Succesfully.")
        task_manager()

    else:
        print("Error: Please try again.")
            

    

    


def update_task():
    
    desc = str(input("Enter Task ID # ([0] for Main Menu ): "))


    if desc == '0':
        task_manager()
    elif desc >= '1':
        time_upd = time.strftime("%a, %d %b %Y %I:%M:%S")
        for i in range(len(task_list)):
            if task_list[i]['ID'] == int(desc):
                c = input("[1] for Task Update or [2] for Status Update: ")
                if c == '1':

                    try:
                        task_list[i]['Task'] = input("Task Update: ")
                        task_list[i]['Time Updated'] = time_upd
                        break
                    except ValueError:
                        print("Error: Please try again.")
                elif c == '2':
                    try:
                        task_list[i]['Status'] = input("Status Update ('todo', 'in-progress', 'done'): ")
                        task_list[i]['Time Updated'] = time_upd
                        break
                    except ValueError:
                        print("Error: Please try again.")
                else:
                    print("Error: Please try again.")


        
        print(f"\nTask updated succesfully. Time: {time_upd}")
        
        task_manager()

    else:

        print("Error: Please try again.")


    







# Main Program Loop

def task_manager():
    while True:
        print("\nHello, Welcome to Task Manager. Please select what you would like to do.")
        print("[1]Create Task\n[2]Update Task\n[3]List Tasks\n[4]Delete Task\n[5]Exit")
        try:
            f = input("Enter: ")
            if f == '5':
                print("Goodbye.")
                sys.exit()
            elif f == '1':
                return create_task()
            elif f == '2':
                update_task()
            elif f == '3':
                if len(task_list) == 0:
                    print("There are currently 0 tasks.\n")
                else:
                    print(json.dumps(task_list, indent=4))
                    t = input('[0] for Main Menu: ')
                    if t == '0':
                        task_manager()
                    else:
                        Print("Error: Please try again.")
            elif f == '4':
                return delete_task()
            else:
                print("Error: Please try again.")

        except ValueError:
            print("Error: Please try again.")

        

if __name__ == '__main__':

    task_manager()


    
