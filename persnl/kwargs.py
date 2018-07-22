def color(first,second,**kwargs):
    return f"{first} favourite color is {second}"
a={'first':'purple','second':'vaibhav'}
print(color(**a,cold='jkjk'))