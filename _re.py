import re

result = dir(re)

# re module

str = "Samed Önder Koçak 40 saat"

# re.findall()

result = re.findall("Samed",str)
result = len(result)

# re.split()
result = re.split(" ",str)
result = re.split("a",str)

# re.sub()
result = re.sub(" ","-",str)
result = re.sub("\s","-",str)

# re.search()
result = re.search("Samed",str)

result = result.span()
result = result.start()
result = result.end()
result = result.group()
result = result.string

# regular expression

result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-e]",str)
result = re.findall("[a-z]",str)
result = re.findall("[0-5]",str)
result = re.findall("[^abc]",str)
result = re.findall("[^0-9]",str)


result = re.findall("...",str)
result = re.findall("Sa..d",str)

result = re.findall("^K",str)

result = re.findall("t$",str)

result = re.findall("sa*t",str)

result = re.findall("sa+t",str)

result = re.findall("sa?t",str)

result = re.findall("a{1,3}",str)
result = re.findall("[0-9]{2}",str)

result = re.findall("\ASamed",str)
result = re.findall("\Zsaat",str)

print(result)