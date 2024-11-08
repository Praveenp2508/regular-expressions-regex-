#regex
#findall
import re
p='data'
t='data science is the part of AI,data science data'
m=re.findall(p,t)
print(m)

a= r'\A+'
b='entr the 123 and 567'
match=re.findall(a,b)
print(match)

fruit=['apple is rs:200','orange price is rs:300','grape price is rs:100']
for i in fruit:
    m=re.findall(r'\d+',i)
    print(m)

fruit=['apple is rs:200','orange price is rs:300','grape price is rs:100']
for i in fruit:
    m=re.findall(r'\w+',i)
    print(m)

fruit=['apple is rs:200','orange price is rs:300','grape price is .rs:100']
for i in fruit:
    m=re.findall(r'\w+|',i)
    print(m)

fruit=['Apple is rs:200','orange Price is rs:300','grape price is .Rs:100']
for i in fruit:
    m=re.findall(r'[A-Z]{1}[a-z]+',i)
    print(m)

fruit=['Apple is rs:200','orange Price is rs:300','grape price is .Rs:100']
for i in fruit:
    m=re.findall(r'\b[A-Za-z]{5}\b+',i)
    print(m)

regex
serach

bag=['banana is the fruit','i dont like banana','Banana is yellow']
for i in bag:
    m=re.search('banana',i)
    print(m)

split
text='india is good'
m=re.split(r'\s',text,2)
print(m)

sub
text='india is good'
m=re.sub(r'\s','=',text)
print(m)

text='apple is rs.300'
m=re.sub(r'rs.','$',text)
print(m)

#match
t='pineapple is the friut and pineapple is tasty and yellow'
m=re.match(r'\w{9}',t)
print(m)




