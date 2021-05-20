def lost_character(a, n):
    if n == 0:
        new_txt = a[n + 1:]
        print(new_txt)
    elif n == len(a):
        new_txt = a[0:n-1]
        print(new_txt)
    else:
        new_txt = a[0:n] + a[n + 1:]
        print(new_txt)


lost_character('kitten', 1)
lost_character('kitten', 4)