
'''
Created By: Caleb Malcarne
Program: Invoice Filler 


'''

import inflect

def num_to_words(num):
    if str(num).isnumeric() == True:
    
        inf = inflect.engine()
        num_ = str(num)
        cents = '00'
        num_striped = '0'
        cents_num = '0'
        dot_pos = '0'
        
        if '.' in num_ and cents_num != '00' or cents_num != '0':
            dot_pos = num_.index('.')
            cents_num = num_[num_.index('.'): len(num_)]
            cents = str(num_[dot_pos  + 1:len(num_)])
            num_striped = num_[0:len(num_)-3]
        else:
            cents = '00'
            num_striped = num_
        
        word_num = inf.number_to_words(int(num_striped)).replace(' and', '')
        
        final_str = f"{word_num} and {cents}/100 Dollars (${num_})"
        return(final_str)
    else:
        return("INVALID INPUT")
        