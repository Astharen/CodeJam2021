import math

def results():
    t = int(input())
    for i in range(1, t+1):
        cj_pay, jc_pay, holed_mural = [s for s in input().split(" ")]
        cj_pay = int(cj_pay)
        jc_pay = int(jc_pay)
        mural = filling_mural(holed_mural, cj_pay, jc_pay)
        value = get_value(mural, cj_pay, jc_pay)
        print (f'Case #{i}: {value}')

def get_best_value_negative(letter, n_times_next_letter, mural):
    if letter == 'C':
        if n_times_next_letter%2==1:
            mural += 'JC' * int(math.ceil(n_times_next_letter/2))[:n_times_next_letter]
        else:
            mural += 'CJ' * int(math.ceil(n_times_next_letter/2))
    else:
        if n_times_next_letter%2==1:
            mural += 'CJ' * int(math.ceil(n_times_next_letter/2))[:n_times_next_letter]
        else:
            mural += 'JC' * int(math.ceil(n_times_next_letter/2))
    return mural

def get_mural_negative_no_first_letter(cj_pay, jc_pay, mural, supp_letter, letter_before):
    if cj_pay>=0 and jc_pay>=0:
        mural += supp_letter       
    if cj_pay<0:
        if letter_before=='C':
            mural += 'J'
        elif letter_before=='J':
            if jc_pay>=0:
                mural += 'J'
    if jc_pay < 0:
        if letter_before=='J':
            mural += 'C'
        elif letter_before=='C':
            if cj_pay >= 0:
                mural += 'C'
    return mural

def filling_mural(holed_mural, cj_pay, jc_pay):
    ind = 0
    supp_letter = 'A'
    mural = ''
    n_times_next_letter = 0
    letter_before = ''
    for letter in holed_mural:
        if letter == '?':
            if supp_letter!='A':
                mural = get_mural_negative_no_first_letter(cj_pay, jc_pay, mural, supp_letter, letter_before)
            else:
                n_times_next_letter += 1

        else:
            if n_times_next_letter > 0:
                if cj_pay>=0 and jc_pay>=0:
                    mural += letter * n_times_next_letter
                elif cj_pay < 0 and jc_pay < 0:
                    mural = get_best_value_negative(letter, n_times_next_letter, mural)
                elif cj_pay >= 0 and jc_pay < 0:
                    if abs(cj_pay) >= abs(jc_pay):
                        mural += 'J' * n_times_next_letter
                    elif abs(cj_pay) < abs(jc_pay):
                        mural = get_best_value_negative(letter, n_times_next_letter, mural)
                elif cj_pay < 0 and jc_pay >= 0:
                    if abs(jc_pay) >= abs(cj_pay):
                        mural += 'C' * n_times_next_letter
                    elif abs(jc_pay) < abs(cj_pay):
                        mural = get_best_value_negative(letter, n_times_next_letter, mural)
                n_times_next_letter = 0
            mural += letter
            supp_letter = letter
        if supp_letter != 'A':
            letter_before = mural[ind]
    return mural


def get_value(mural, cj_pay, jc_pay):
    value = 0
    for i in range(len(mural)-1):
        if mural[i:i+2] == 'CJ':
            value += cj_pay
        elif mural[i:i+2] == 'JC':
            value += jc_pay
    return value


results()