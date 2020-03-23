start_message = 'Input int number:'
error_message = 'Wrong value. Input int number:'
end_message = 'Thank you.'


def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        n = input()
        try:
            n = int(n)
        except:
            print(error_message)
        else:
            print(end_message)
            break
    return n
