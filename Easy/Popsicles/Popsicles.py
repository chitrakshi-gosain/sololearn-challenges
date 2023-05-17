siblings_count = int(input())
popsicles_count = int(input())

print('give away') if popsicles_count % siblings_count == 0 else print('eat them yourself')