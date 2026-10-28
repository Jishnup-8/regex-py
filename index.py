import re

# re.match(pattern , string)
#1).. Re.match...

# text = 'python is easy '
# text = 'the python is easy '


# result = re.match('python' , text)
# if result:
#     print('Match found')
# else :
#     print('No match')

# 2 ) re.search()
# text = 'Python is easy and java also'

# result = re.search('easy' , text)
# if result :
#     print('Match found')
# else :
#     print('No match')

# text = 'Python is easy and java also'

# result = re.search('javascript' , text)
# if result :
#     print('Match found')
# else :
#     print('No match')

# 3)  re.finadall() => all matches pattern as list 

# text = 'python is easy and java also , but python i simple , python is good'
# result  = re.findall('python' , text)

# print(result)


# text = 'python is easy and java also , but python is simple , python is good'
# result  = re.findall('is' , text)

# print(result)

# text = "mark : 85 90 78 95"
# numbers = re.findall(r'\d+' , text)
# # # \d => digits 0-9 
# # # + => one or more items 
# print(numbers)

# 3 ) re.split() => transform into list...
# text = 'Apple , Banana , Mango'
# result = re.split(',' , text)
# print(result)

# text = "python javascript java c c++"
# result = re.split(' ',text)
# print(result) 

# 4 ) re.sub() => replace all matches patterns ..
text = 'python is easy'
# print(text)
result = re.sub('python','javascript',text)
print(result)

text = 'order Id : 238725'
result = re.sub(r"\d" ,"*" , text)
print(result)

