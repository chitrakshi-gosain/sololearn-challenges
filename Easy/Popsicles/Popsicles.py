siblings_count = int(input())
popsicles_count = int(input())

MESSAGE = 'give away' if popsicles_count % siblings_count == 0 else 'eat them yourself'
print(MESSAGE)
