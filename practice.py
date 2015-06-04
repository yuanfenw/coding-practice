def longest_substr(a, num_char=2):
    len_i = [0]*len(a) # or use list comprehesion
    for i in xrange(len(a)):
        j=i
        curr_chars=set([a[i]])
        number_unique=1
        while (j<len(a)-1 or number_unique<=num_char):    
            if a[j] not in curr_chars: # if the character is not in the set yet, add it
                curr_chars.add(a[j])
                number_unique=number_unique+1
            j=j+1
        len_i[i] = j-i+1
        print(curr_chars)
        print(len_i[i])
    return max(len_i)
                

longest_substr(a)
         


#output the most frequence n numbers in a array

def most_freq(a, n):
    num_count <- default_dict(a)
    
    

def breadth_first_search(root_nd):
    
    a=[root_nd]
    visited = set()
    while not a:
        top=a.top()
        a.pop()
        if top not in visited:
            visited.add(top)
            for nb in n.get_nb():
                if nb not in visited:
                 a.push(nb)
             