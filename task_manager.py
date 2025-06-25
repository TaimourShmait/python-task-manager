def insert(queue : list, priority, task):
    queue.append((priority, task))

def extract(queue : list, index = 0): # Remove the first item in the queue if the index is not passed
    return queue.pop(index)

def peek(queue : list): 
    return queue[0]

def is_empty(queue : list):
    return len(queue) == 0

def complete_next_task(queue : list):
    highest_priority_task = queue[0]
    highest_priority_index = 0
    if not is_empty(queue):
        for i in range(len(queue)):
            if queue[i][0] < highest_priority_task[0]: # Comparing the priorites
                highest_priority_task = queue[i]
                highest_priority_index = i

        print("\nCompleted the following task: " + str(extract(queue, highest_priority_index)) + "\n")  
    else:
        print("\nThe queue is empty!\n")

def search_for_task(queue : list, title):
    # Binary search cannot be used in this specific use case, use linear search instead
    sorted_queue = sort_tasks(queue)

    for task in sorted_queue:
        if task[1][0].lower() == title.lower():
            return task
    return "Task with title '" + title + "' was not found!"

def sort_tasks(queue: list):
    # Sorted by duration - asending
    sorted_queue = queue[:]

    for i in range(len(sorted_queue)):
        for j in range(len(sorted_queue)):
            if sorted_queue[i][1][1] < sorted_queue[j][1][1]:
                temp = sorted_queue[i]
                sorted_queue[i] = sorted_queue[j]
                sorted_queue[j] = temp
    return sorted_queue
        
task_count = int(input("Enter number of tasks: "))

while task_count <= 0:
    task_count = int(input("Enter a valid number of tasks: "))

tasks = []

for i in range(task_count):
    task = ()

    title = input("Enter task title for task " + str(i + 1) + ": ")
    while len(title) == 0 or title == "" or (not title):
        title = input("Enter a valid title for task " + str(i + 1) + ": ")

    duration = int(input("Enter task duration for task " + str(i + 1) + ": "))
    while duration <= 0:
        duration = int(input("Enter a valid duration for task " + str(i + 1) + ": "))

    priority = int(input("Enter task priority for task " + str(i + 1) + ": "))
    while priority < 0:
        priority = int(input("Enter a valid priority for task " + str(i + 1) + ": "))

    task = (title, duration)
    insert(tasks, priority, task)

print("\nUnsorted tasks:\n" + str(tasks) + "\n")
print("Tasks sorted by duration (ascending):\n" + str(sort_tasks(tasks)))

search_title = input("\nSearch for a task by title: ")
print(search_for_task(tasks, search_title))

complete_next_task(tasks)
print("Tasks remaining:\n" + str(tasks))