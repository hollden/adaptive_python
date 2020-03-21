import sys

old_file = r'/home/atarasov/Working/blok_users.sql'
new_file = r'/home/atarasov/Working/blok_users_new.sql'

# with open(old_file, 'r') as f:
#     for line in f:
#         arr = line.split()
#         arr[2] = '"' + arr[2] + '"'
#         print(arr)
#         with open(new_file, 'a') as g:
#             g.write(' '.join(arr))
#             g.write('\n')
#


def main():
    print('arguments: ', sys.argv)


if __name__ == '__main__':
    main()