import threading
counter =0

def increasing_counter():
    global counter
    for _ in range (100000):
        counter +=1


def decreasing_counter():
    global counter
    for _ in range (100000):
        counter -=1


thread1 = threading.Thread(target=increasing_counter)
thread2 = threading.Thread(target=decreasing_counter)



thread1.start()
thread2. start()



thread1.join()
thread2.join()


print("the counter is:" counter)

