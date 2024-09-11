import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            sys.stdout.write('-1' + '\n')
        else:
            sys.stdout.write(str(stack.pop()) + '\n')
    elif command[0] == 'size':
        sys.stdout.write(str(len(stack)) + '\n')
    elif command[0] == 'empty':
        if len(stack) == 0:
            sys.stdout.write('1' + '\n')
        else:
            sys.stdout.write('0' + '\n')
    elif command[0] == 'top':
        if len(stack) == 0:
            sys.stdout.write('-1' + '\n')
        else:
            sys.stdout.write(str(stack[len(stack) - 1]) + '\n')