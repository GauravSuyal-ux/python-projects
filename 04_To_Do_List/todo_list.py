todo_list=[]

while True:
    print ("==== Terminal Based To Do List ====")
    print("Menu-\n1.Add Task\n2.View Tasks\n3.Delete Task\n4.Exit")

    try:
        user_choice=int(input("Enter your choice (1-4):"))
    except ValueError:
        print("Invalid Choice! Please enter a number")
        continue
    if user_choice==1:
        task=input("Please enter your task:").strip()
        todo_list.append(task)
        print("Task added Successfully")
    elif user_choice==2:
        if len(todo_list)==0:
            print("No Tasks Available.")
        else:
            counter=1
            for task in todo_list:
                print(f"{counter}.{task}")
                counter+=1
                
