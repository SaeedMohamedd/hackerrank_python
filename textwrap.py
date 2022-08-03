import textwrap
def wrap(string,max_width):
    return '\n'.join(textwrap.wrap(string,max_width))


#___________________without textwrap____________________________
def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])



#return "/n".join([string[i:i+max_width]for i in range(0,len(string),max_width)])
#___________________mysolution______________________________________

def wrap(string, max_width):
    s=""
    count =0
    for i in string :
        s+=i
        count +=1
        if count == max_width:
            s+='\n'
            count=0
        
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    #result = wrap(string, max_width)
    result = wrap(string, max_width)
    print(result)

