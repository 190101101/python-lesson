from string import Template

p1 = 'cookie'
p2 = 'kikusi'

p3 = Template("$p2's real name is $p1")
print(p3.substitute(p1=p1, p2=p2))