import textwrap

def merge_the_tools(string, k):
    # your code goes here
    wrapper = textwrap.TextWrapper(width = k)
    word_list = wrapper.wrap(text=string)
    for x in word_list:
        print("".join(dict.fromkeys(x)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)