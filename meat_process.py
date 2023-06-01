import threading
import time
import random

class MeatProcessingFactory:
    # Declare number of servings as stated in question
    # Lock used for synchronization to ensure mutex
    def __init__(self):
        self.beef_servings = 10
        self.pork_servings = 7
        self.chicken_servings = 5
        self.beef_lock = threading.Lock()
        self.pork_lock = threading.Lock()
        self.chicken_lock = threading.Lock()
        self.output_file = open("output.txt", "w")

    # Ensure mutex with call the Lock
    def process_beef(self, employee):
        with self.beef_lock:
            if self.beef_servings > 0:
                self.beef_servings -= 1
                output = f"{employee} picked beef at {time.strftime('%H:%M:%S')}. Beef servings left: {self.beef_servings}.\n"
                print(output)
                self.output_file.write(output)
                time.sleep(1)
                output = f"{employee} processed beef at {time.strftime('%H:%M:%S')}.\n"
                print(output)
                self.output_file.write(output)
            else:
                output = f"{employee} can't find beef.\n"
                print(output)
                self.output_file.write(output)

    def process_pork(self, employee):
        with self.pork_lock:
            if self.pork_servings > 0:
                self.pork_servings -= 1
                output = f"{employee} picked pork at {time.strftime('%H:%M:%S')}. Pork servings left: {self.pork_servings}.\n"
                print(output)
                self.output_file.write(output)
                time.sleep(2)
                output = f"{employee} processed pork at {time.strftime('%H:%M:%S')}.\n"
                print(output)
                self.output_file.write(output)
            else:
                output = f"{employee} can't find pork.\n"
                print(output)
                self.output_file.write(output)

    def process_chicken(self, employee):
        with self.chicken_lock:
            if self.chicken_servings > 0:
                self.chicken_servings -= 1
                output = f"{employee} picked chicken at {time.strftime('%H:%M:%S')}. Chicken servings left: {self.chicken_servings}.\n"
                print(output)
                self.output_file.write(output)
                time.sleep(3)
                output = f"{employee} processed chicken at {time.strftime('%H:%M:%S')}.\n"
                print(output)
                self.output_file.write(output)
            else:
                output = f"{employee} can't find chicken.\n"
                print(output)
                self.output_file.write(output)

# Main function will first declare the employees and related tasks as declared in MeatProcessingFactory class.

def main():
    factory = MeatProcessingFactory()

    employees = ["A", "B", "C", "D", "E"]
    tasks = [factory.process_beef, factory.process_pork, factory.process_chicken]

    threads = []
    while factory.beef_servings > 0 or factory.pork_servings > 0 or factory.chicken_servings > 0: # loop until each task is completed
        random.shuffle(tasks)
        for i, employee in enumerate(employees):
            task = tasks[i % len(tasks)] # loop with max = len(tasks)
            thread = threading.Thread(target=task, args=(employee,)) # create thread w.r.t. task and employee
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join() # main thread wait for each thread to finish
        threads.clear()

if __name__ == '__main__':
    main()