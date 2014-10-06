# range(start, stop[, step])
for i in range(0,5):
    print i;
print '==============';

for i in range(0,5,2):
    print i;
print '==============';

for i in [0, 1, 2]:
    print i;
print '=====for end =========';

i =  0;
while i < 5:
    print i;
    i+=1;

print '==============';

i =  0;
while True:
    if i >= 5:
        break;
    else:
        i+=1;
        if i % 2 == 1:
            continue;
        print i;

print '==============';