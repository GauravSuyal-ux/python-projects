todo_list=[]

def view_tasks():
    if len(todo_list)==0:
            print("No Tasks Available.")
    else:
        counter=1
        for task in todo_list:
            print(f"{counter}.{task}")
            counter+=1
                

while True:
    print ("==== Terminal Based To Do List ====")
    print("Menu-\n1.Add Task\n2.View Tasks\n3.Delete Task\n4.Edit Task\n5.Clear All Tasks\n6.Exit")

    try:
        user_choice=int(input("Enter your choice (1-5):"))
    except ValueError:
        print("Invalid Choice! Please enter a number")
        continue

    if user_choice==1:
        task=input("Please enter your task:").strip()
        todo_list.append(task)
        print("Task added Successfully")


    elif user_choice==2:
        view_tasks()
                
    elif user_choice==3:
         while True:
            if len(todo_list)==0:
                print("Sorry! No tasks available")
                break
            
            else:
                view_tasks()
                try:
                    user_input=int(input(f"Enter the no. of task from 1-{len(todo_list)}which you want to delete: "))
                except ValueError:
                    print("Please enter a valid integer:")
                    continue
            
                if 1 <= user_input <= len(todo_list):
                    removed_task=todo_list.pop(user_input-1)
                    print(f"Task '{removed_task}' deleted successfully")
                    break
                else:
                    print(f"Please enter the number which is >=1 and <={len(todo_list)}")

    elif user_choice==4:
        
        if len(todo_list)==0:
            print("No task Available ")
        else:
            while True:
                view_tasks()
                try:
                    user_edit_input=int(input(f"Enter the no. of task from 1-{len(todo_list)} which you want to edit: "))
                except ValueError:
                    print("Enter a valid integer")
                    continue
            
                if  1<=user_edit_input<=len(todo_list):
                    new_input=input("Enter the new task which you want to edit:")
                    todo_list[user_edit_input-1]=new_input
                    print("Task edited successfully")
                    break
                else:
                    print(f"Enter the number from 1- {len(todo_list)}:")

    elif user_choice==5:
        if len(todo_list)==0:
            print("No Tasks Available")
        else:
            print("Available Tasks:")
            view_tasks()
            while True:
                user_ans1=input("This will permanently delete all tasks. Continue? (y/n):").lower().strip()
                if user_ans1=="y":
                    user_ans2=input("Are you absolutely sure? (y/n):").lower().strip()
                    if user_ans2=="y":
                        todo_list.clear()
                        print("Tasks deleted successfully..")
                        break
                    elif user_ans2=="n":
                        print("Operation Cancelled..")
                        break
                    else:
                        print("Invalid Input! Please enter '(y/n)':")
                elif user_ans1=="n":
                    print("Operation Cancelled..")
                    break
                else:
                    print("Invalid input! Please enter '(y/n)':")
    
    elif user_choice==6:
        print("Thanks for using To-Do list. Goodbye!")
        break

    