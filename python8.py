import math
def get_centrs():
    circ_num = int(input('Chiselko okrujnostey: '))
    if (circ_num <= 1):
        print('ERR!!!: nekrasivoe chiselko: {}'.format(circ_num))
        return 0
    centrs = [(float(input('Okrujnost {}: text pls X of centr: '.format(i+1))), float(input('Okrujnost {}: text pls Y of centr: '.format(i+1)))) for i in range (0, circ_num)]
    for i,c in enumerate(centrs):
        for i_,c_ in enumerate(centrs):
            if (c == c_ and i != i_):
                print('ERR!!!: 2 okrujnosty s obshim centrom, tak nizya(((.')
                return 0
    return centrs

def circ_imp(circles):
    circ_r = [[circle, 0] for circle in circles]
    '''Евклидово расстояние'''
    def dist(circle_1, circle_2):
        return math.sqrt(sum(list(map(lambda x,y: (x-y)**2, circle_1[0], circle_2[0]))))
    '''Максимальное расстояние между кругами для дальнейшего сравнения'''
    max_dist = 0
    for c in circ_r:
        for c_ in circ_r:
            d = dist(c, c_)
            if (d > max_dist):
                max_dist = d
    '''Нахождение для текущего круга соседа, столкновение с которым наиболее близко'''
    def closest_imp(circle):
        min_d = max_dist
        nn = None #nearest neighbour
        for c in circ_r:
            if (c != circle):
                if (c[1] == 0):
                    d = dist(c, circle)/2
                else:
                    d = dist(c, circle) - c[1]
                if (d <= min_d):
                    min_d = d
                    nn = c
        return nn
    '''Вычисление первого столкновения для определённости сисетмы'''
    c1, c2 = None, None
    min_d = max_dist
    for c in circ_r:
        for c_ in circ_r:
            if (c[0] != c_[0]):
                d = dist(c, c_)
                if (d < min_d):
                    c1, c2 = c, c_
                    min_d = d
    if (len(circles) > 2):
        for a in circ_r:
            if (a[0] == c1[0]):
                a[1] = min_d/2
            if (a[0] == c2[0]):
                a[1] = min_d/2
    for circle in circ_r:
        if (circle[1] != 0):
            continue
        nearest_neighbour = closest_imp(circle)
        if (nearest_neighbour[1] == 0):
            d = dist(nearest_neighbour, circle)/2
            circle[1] = d
            for n in circ_r:
                if n == nearest_neighbour:
                    n[1] = d
        else:
            d = dist(nearest_neighbour, circle) - nearest_neighbour[1]
            circle[1] = d
    return circ_r

def autotest():
    test_arr = [(0,0), (0,1), (3,0)]
    test_rads = circ_imp(test_arr)
    if (test_rads[0][1] != 0.5 or test_rads[1][1] != 0.5 or test_rads[2][1] != 2.5):
        print('ERR!!!: Nekrasivo(((((((\n')
        raise SystemExit(-1)
    print('Krasivo)))))))')
    
autotest()

test = get_centrs()
rads = circ_imp(test)
print(rads)