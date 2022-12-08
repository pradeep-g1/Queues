class Queue:
    def __init__(self,cap):
        self.queue=[None]*cap
        self.front=None
        self.rear=None
        self.capacity=cap
    def isfull(self):
        if self.rear==self.capacity-1:
            print("Overflow condition, cant enque")
        return self.rear==self.capacity-1
    def is_empty(self):
        if self.front is None:
            print("Underflow condition cant deque :")
        return self.front is None
    def enqueue(self,item):
        if self.isfull():
            return
        if self.front is None:
            self.front=0
            self.rear=0
        else:
            self.rear+=1     
        self.queue[self.rear]=item
        print(self.queue[self.rear]," enqueued to queue")
    def deque(self):
        if self.is_empty():
            return 
        item=self.queue[self.front]
        self.front+=1
        #resetting the queue when the last item is deuqued
        if self.front>self.rear:
            self.front=self.rear=None
        print(item," deueued from queue")
    #function to display the queue
    def display(self):
        if self.rear is None:
            print("Queue was empty")
        else:
            i = self.front
            print("Queue :",end=" ")
            while i<=self.rear:
                print(self.queue[i],end=" ")
                i+=1
q=Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print()
q.deque()
q.deque()
q.enqueue(60)
print()
q.display()
print()