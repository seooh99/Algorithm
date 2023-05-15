# vowels = ['a', 'e', 'i', 'o', 'u']
#
# while True:
#     check = 'false'
#     word = input()
#     if word == 'end':
#         break
#     # '모음 하나를 반드시 포함' 조건 확인
#     if all(i not in vowels for i in word):
#         print(f'<{word}> is not acceptable.')
#         check = 'true'
#         continue
#
#     lst = list(word)
#     if len(lst) >= 3:
#         for i in range(len(lst)):
#             if lst[i] in vowels:
#                 if i + 2 < len(lst):
#                     if lst[i+1] in vowels and lst[i+2] in vowels:
#                         print(f'<{word}> is not acceptable.')
#                         check = 'true'
#                         break
#
#             elif lst[i] not in vowels:
#                 if i + 2 < len(lst):
#                     if lst[i+1] not in vowels and lst[i+2] not in vowels:
#                         print(f'<{word}> is not acceptable.')
#                         check = 'true'
#                         break
#
#         if check == 'true':
#             break
#
#     if len(lst) >= 2:
#         for i in range(len(lst) - 1):
#             if lst[i] == 'e' or lst[i] == 'o':
#                 if lst[i] == lst[i + 1]:
#                     pass
#             elif lst[i] == lst[i+1]:
#                 print(f'<{word}> is not acceptable.')
#                 check = 'true'
#                 break
#
#         # 만약 마지막 조건도 통과했다면 acceptable
#         else:
#             print(f'<{word}> is acceptable.')
#     # 모두다 통과했다면 acceptable
#     else:
#         print(f'<{word}> is acceptable.')


vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    check = False
    word = input()
    if word == 'end':
        break
    # '모음 하나를 반드시 포함' 조건 확인
    if all(i not in vowels for i in word):
        print(f'<{word}> is not acceptable.')
        check = True
        continue

    lst = list(word)
    if len(lst) >= 3:
        for i in range(len(lst)):
            if lst[i] in vowels:
                if i + 2 < len(lst):
                    if lst[i+1] in vowels and lst[i+2] in vowels:
                        print(f'<{word}> is not acceptable.')
                        check = True
                        break

            elif lst[i] not in vowels:
                if i + 2 < len(lst):
                    if lst[i+1] not in vowels and lst[i+2] not in vowels:
                        print(f'<{word}> is not acceptable.')
                        check = True
                        break

        if check:
            continue

    if len(lst) >= 2:
        for i in range(len(lst) - 1):
            if lst[i] == 'e' or lst[i] == 'o':
                if lst[i] == lst[i + 1]:
                    pass
            elif lst[i] == lst[i+1]:
                print(f'<{word}> is not acceptable.')
                check = True
                break

        # 만약 마지막 조건도 통과했다면 acceptable
        if not check:
            print(f'<{word}> is acceptable.')
    # 모두다 통과했다면 acceptable
    else:
        print(f'<{word}> is acceptable.')



