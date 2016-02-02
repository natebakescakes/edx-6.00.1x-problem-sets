s = 'azcbobobegghakl'

count = 0

for i, char in enumerate(s):
    if s[i:i+3] == 'bob':
        count += 1
        
print ('Number of times bob occurs is: %d' % count)