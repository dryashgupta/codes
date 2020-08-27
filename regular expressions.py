import re
print(sum ( [ int(line) for line in re.findall('[0-9]+',open('actual.txt').read()) ] ) )
