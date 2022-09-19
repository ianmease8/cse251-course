# TODO import the appropriate threading and thread modules
from cse251 import Log
import threading
# TODO create a global counter

sum_global = 0
# TODO create a summing function that to target using the threading module.

def sum(number, Log):
    global sum_global
    sum_global = 0
    for x in range(0, number):
        sum_global += x
# TODO create a class that extends the Thread class (make sure you use a constructor
#  and have a run function)

class MyThread(threading.Thread):

    def __init__(self, number):
        threading.Thread.__init__(self)
        print(f'{self.name} is being created \n', end="")
        self.sum = 0
        self.number = number

    def print_message(self, number):
        for x in range(number):
            self.sum += x
            print(f'{self.name}, {self.sum=} \n', end="")

    def run(self):
        print(f'{self.name} starting \n', end="")
        self.print_message(self.number)
        print(f'{self.name} ending \n', end="")
        return self.sum


# Note: don't change the name of this function or the unit test won't work
def create_threads(number, Log):
    ''' number = the range to sum over, so if numbers equals 10, 
        then the sum will be 1 + 2 + ... + 9 + 10 = 45 
    '''
    Log.write(f'number={number}')

    # Two ways to create a thread:
    # 1) Create a class that extends Thread and then instantiate that class
    thread1 = MyThread(number)
    thread1.start()
    thread1.join()
    sum_numbers_object = thread1.sum
    print(sum_numbers_object)
    # 2) Instantiate Thread and give it a target and arguments
    thread2 = threading.Thread(target=sum, args=(number,Log,))
    thread2.start()
    thread2.join()
    print(f' {sum_global}')
    # LEAVE THIS so that your code can be tested against the unit test
    # (you can change the name of these variables)
    return  sum_numbers_object, sum_global

# Leave this so that you can run your code without needed to run the unit test.
# Once you believe it is working, run the unit test (challenge01_test.py) to 
# verify that it works against more numbers than 10.
if __name__ == '__main__':
    log = Log(show_terminal=True)
    create_threads(10, log)
