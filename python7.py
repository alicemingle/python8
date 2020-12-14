def obiedinim (segment, t_1, t_2):
    a = min(segment[t_1][0], segment[t_2][0])
    b = max(segment[t_1][1], segment[t_2][1])
    segment[t_1] = [a,b]
    return segment

def sravnim (segment, t_1, t_2):
    if (segment[t_1][0] <= segment[t_2][0] <= segment[t_1][1]) or (segment[t_1][0] <= segment[t_2][1] <= segment[t_1][1]):
        return True
    else:
        return False
                             
def otsortiruem (segment):
    segment = sorted(segment, key = lambda x: x[0], reverse = False)
    segment = sorted(segment, key = lambda x: x[1], reverse = False)
    return segment

def ismerim (segment, num):
    for i in range(num):
        for j in range(num):
            if (sravnim(segment,i,j) == True):
                obiedinim(segment, i,j)
    return segment

def longest (segment, num):
    segment_length = []
    for i in range(num):
        segment_length.append(segment[i][1] - segment[i][0])
    x = max(segment_length)
    i = []
    i_x = indekses(segment_length.copy(), x)
    return i_x

def indekses (segment, kek):
    result = []
    for i in range(len(segment)):
        if (segment[i] == kek):
            result.append(i)
    return result

def autotest():
    s = True
    segment = [[3,4], [2,3], [1,3], [1,2]]
    segment_1 = obiedinim(segment.copy(), 1,2)
    t_1 = sravnim(segment, 2,3)
    segment_2 = otsortiruem(segment.copy())
    segment_3 = ismerim(segment_2.copy(),4)
    t_2 = longest(segment_3,4)
    if segment_1 != [[3, 4], [1, 3], [1, 3], [1, 2]] or t_1 != True or segment_2 != [[1,2], [1,3], [2,3], [3,4]] or segment_3 != [[1, 4], [1, 4], [2, 4], [1, 4]] or t_2 != [0, 1, 3]:
        s = False
    if s == True:
        print("K R A S I V O))))))")
    else:
        print("ERR: N E K R A S I V O((((((")

num = int(input("Skolko otrezochkoff: "))
if num == 0:
    print("ERR: Nekrasivoe chiselko otrezochkoff")
    exit(-2)
segment = []
for i in range(num):
    print("Napishite pls for", i+1, "otrezochka")
    a = int(input("Pravii end: "))
    b = int(input("Levii end: "))
    if (a < b):
        segment.append([a,b])
    else:
        print("ERR: Eto ne otrezochek!!!")
        exit(-1)
        
segment_2 = otsortiruem(segment)
segment_1 = ismerim(segment_2.copy(), num)
m = []
m = longest(segment_1, num)
for j in m:
    print("Otvetik:", segment_1[j], "Itogovaya dlina:", segment_1[j][1] - segment_1[j][0])
autotest()