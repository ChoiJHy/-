import sys

n = int(sys.stdin.readline())

# queue = [0 for i in range(2000000) ]
max_size = 2000001
queue = [0] * max_size
front = rear = 0 # queue의 인덱스를 가르킬 front와 rear, 입력을 받으면 rear가 움직이고, 출력은 front에서 진행

def Empty():
    global front, rear
    if front != rear:
        return 0
    return 1


def IsFull():
    global front, rear, max_size
    if (rear + 1) % max_size == front:
        return True
    return False

def Size():
    global front, rear, max_size
    return rear - front if rear >= front  else (rear - front) + max_size

def Push(n):
    global queue, front, rear, max_size
    if not IsFull():
        rear = (rear + 1) % max_size
        queue[rear] = n

def Pop():
    global queue, front, rear, max_size
    if not Empty():
        front = (front + 1) % max_size
        value = queue[front]
        return value
    return -1

def Front():
    global front, queue
    if not Empty():
        return queue[front + 1]
    return -1

def Back():
    global queue, rear
    if not Empty():
        return queue[rear]
    return -1

for i in range(n):
    command = sys.stdin.readline().split()

    if 'push' == command[0]:
        Push(command[1])
    elif 'pop' == command[0]:
        sys.stdout.write(str(Pop()) + '\n')
    elif 'size' == command[0]:
        sys.stdout.write(str(Size()) + '\n')
    elif 'empty' == command[0]:
        sys.stdout.write(str(Empty()) + '\n')
    elif 'front' == command[0]:
        sys.stdout.write(str(Front()) + '\n')
    elif 'back' == command[0]:
        sys.stdout.write(str(Back()) + '\n')