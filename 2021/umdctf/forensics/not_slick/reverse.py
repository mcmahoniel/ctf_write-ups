with open('notslick.png', 'rb') as fp_in:
    reversed_data = fp_in.read()[::-1]
    with open('reversed.png', 'wb') as fp_out:
        fp_out.write(reversed_data)
