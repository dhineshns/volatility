import main as main
import collections as coll


def t_is_more_than_n_percent_different():
    res = main.is_more_than_n_percent_different([1,2,3,4,5], 0, 3, 5)
    if(res != [True, 300.0]):
        print("Fail")
    res = main.is_more_than_n_percent_different([1, 1, 1, 1, 1], 0, 3, 5)
    if (res != [False, 0.0]):
        print("Fail")
    print("Done")

def t_append_to_fixed_len_queu():
    res = main.append_to_fixed_len_queu(coll.deque([1,2,3,4,5]), 6, 5)
    if(res != coll.deque([6,1,2,3,4])):
        print("Fail")
    res = main.append_to_fixed_len_queu(coll.deque([1]), 6, 5)
    if (res != coll.deque([6, 1])):
        print("Fail")
    print("Done")

if __name__ == '__main__':
    t_is_more_than_n_percent_different()
    t_append_to_fixed_len_queu()