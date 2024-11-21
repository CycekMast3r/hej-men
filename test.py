# def swapMaxMin(list):

#     max_value = max(list)
#     min_value = min(list)

#     for number_index, number in enumerate(list):
#         if number == max_value:
#             list[number_index] = min_value

#         if number == min_value:
#             list[number_index] = max_value
    
#     return list

# if __name__ == "__main__":
#     lista= [3, 8, 2, 1, 6, 7, 8, 5, 1, 4, 1, 8, 1]  
#     print(lista)

#     modified_lista = swapMaxMin(lista)
#     print(modified_lista)

#zad 2 

# def reverse_list_string(lista):
#     reversed_list = []

#     for word in lista:
#         reversed_list.append(word.swapcase())        
    
#     return reversed_list[::-1]


# if __name__ == "__main__":
#     lista = ["Python", "JavaScript", "Java", "HTML"]
#     print(reverse_list_string(lista))

#zad 3

# def union_list(list1, list2):
#     sum_list = []
    
#     sum_list = list(set(list1 + list2))
#     sum_list.sort(reverse=True)

#     return sum_list

# if __name__ == "__main__":
#     list1 = [1, 2, 5, 3, 4, 2, 5, 4, 3, 10]
#     list2 = [3, 4, 5, 6, 3, 8, 7, 10] 

#     print(union_list(list1,list2))

#zad4
# import random

# def generate_list():
#     n = random.randint(1,15)
#     print(n)
#     random_list = []

#     for _ in range(n):
#         random_num = random.randint(1,50)
#         random_list.append(random_num)

#     return random_list

# if __name__ == "__main__":
#     list = generate_list()

#     print(list)
#     print(max(list))
#     print(min(list))
#zad 5

def count_all_words(sentence: str):
    words_amount = len(sentence.split())
    return words_amount

def count_word(
        sentence: str, 
        word:     str    
)       ->        int:

    lower_sentence = sentence.lower()
    lower_word = word.lower()
    word_repetition = lower_sentence.count(lower_word)

    return word_repetition

def change_word(
        sentence:   str,
        word:       str
)       ->          str:
    
    word_upper = word.upper()
    words = sentence.split()

    for i in range(len(words)):
        if words[i].lower() == word.lower():
            words[i] = word_upper
            
    return ' '.join(words)

if __name__ == "__main__":
    sentence = 'PYTHON. To jest kolokwium z przedmiotu Programowanie skryptowe, które wykorzystuje język pythonPythonPYTHON. PythoN jest nie OK. PYtHOn'
    print(count_all_words(sentence))
    print(count_word(sentence, 'python'))
    print(change_word(sentence, 'python'))
