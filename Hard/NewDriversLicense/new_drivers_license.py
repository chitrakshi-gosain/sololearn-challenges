target_name = input()
agent_count = int(input())
queue = input().split(' ')

queue.append(target_name)
queue.sort()

print(20 * (1 + queue.index(target_name) // agent_count))
