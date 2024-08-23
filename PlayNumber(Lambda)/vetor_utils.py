

import functools

def myStrip(function, iterable):
    pass

def mysplit(function, iterable):
    pass


def myfilter(function, iterable):
        
        ListaNova = []

        for elements in iterable:
            if function(elements):
                ListaNova.append(elements)

        return ListaNova

def myMap(function, iterable):
    
    ListaNova = []

    for elements in iterable:
        ListaNova.append(function(elements))
        
    return ListaNova

def myReduce(function, iterable):

    ValorFinal = 0

    for elements in iterable:
        ValorFinal += function(elements)
    
    return ValorFinal

def main():

    ListNumber = [1, 2, 3, -4, 100, 0, 48]

    print(myReduce(lambda x,y: x + y, ListNumber))

main()