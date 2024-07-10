from threading import Thread
import queue
from time import sleep

class Table():
    def __init__(self,number):
        self.number = number
        self.is_busy = False


class Customer():
    def __init__(self, name):
        self.name = "Посетитель " + str(name+1)


class Cafe(Thread):
    def __init__(self,queue,queue_t):
        super().__init__()
        self.queue = queue
        self.queue_t = queue_t

    def customer_arrival(self):

        for i in range(len(customer)):
            cust = customer[i]
            print(f"{cust} прибыл")

            nft = 0
            for i in range(len(tables)):
                if tables[i][1] == False:
                    nft = i +1
                    print(f"{cust} сел за стол {nft}")
                    tables[i][1] = True
                    tables[i][2] = cust
                    self.queue_t.put(cust)
                    break

            if nft == 0:
                print(f"{cust} ожидает свободный стол")
                self.queue.put(cust)
                sleep(0.1)

        for i in range(len(tables)):
            queue.put(None)


    def serve_customer(self):

        while queue_t.qsize():
            sleep(0.2)
            cust_end = queue_t.get()
            cust = queue.get()

            nft = 0
            for i in range(len(tables)):
                if tables[i][2] == cust_end:
                    nft = i
                    print(f"{cust_end} поел и ушел. Стол {nft+1} свободен")
                    tables[i][1] = False
                    tables[i][2] = "Empty"
                    if cust != None:
                        print(f"{cust} сел за стол {nft+1}")
                        tables[i][1] = True
                        tables[i][2] = cust
                        self.queue_t.put(cust)
                    break

            queue.task_done()
            queue_t.task_done()


queue_t = queue.Queue()
queue = queue.Queue()


t1 = Table(1)
t2 = Table(2)
t3 = Table(3)
tables = [[t1.number, t1.is_busy, 'Empty'], [t2.number, t2.is_busy, 'Empty'], [t3.number, t3.is_busy, 'Empty']]

customer = []

for i in range(20):
    cust = Customer(i)
    customer.append(cust.name)

cafe = Cafe(queue, queue_t)

customer_arrival_thread = Thread(target=cafe.customer_arrival)
serve_customer_thread = Thread(target=cafe.serve_customer)

customer_arrival_thread.start()
serve_customer_thread.start()

customer_arrival_thread.join()
serve_customer_thread.join()
