import copy


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cap(a):
    return -a[1], a[0]


def diff(a, b):
    return (a[0] - b[0]), (a[1] - b[1])


def add(a, b):
    return (a[0] + b[0]), (a[1] + b[1])


def triangle_area(a, b, c):
    return dot(diff(c, a), cap(diff(b, a)))


def point_left_to_line(q, p1, p2):
    return dot(diff(q, p1), cap(diff(p2, p1))) >= 0


def is_ccw(points):
    length = len(points)
    sum = (points[0][0] - points[length - 1][0]) * (points[0][1] + points[length - 1][1])
    for i in range(1, length):
        sum += (points[i][0] - points[i - 1][0]) * (points[i][1] + points[i - 1][1])
    return sum < 0


def is_convex(v_prev, v, v_next):
    return triangle_area(v_prev, v, v_next) > 0


def no_vertex_in_triangle(points, v_prev, v, v_next):
    for w in points:
        if w == v or w == v_prev or w == v_next:
            continue
        if point_left_to_line(w, v_prev, v) and point_left_to_line(w, v, v_next) and point_left_to_line(w, v_next, v_prev):
            return False
    return True


def is_ear(points, v_prev, v, v_next):
    return is_convex(v_prev, v, v_next) and no_vertex_in_triangle(points, v_prev, v, v_next)


def ears_finding(points):
    ears = []
    if not is_ccw(points):
        points.reverse()
        rev = True
    length = len(points)
    for i in range(0, length):
        if is_ear(points, points[(i - 1) % length], points[i], points[(i + 1) % length]):
            ears.append(points[i])
    return ears, rev


def ears_clipping(points, ears, outputtype, rev):
    edges = []
    length = len(points)
    if outputtype == "index":
        all_points = copy.deepcopy(points)
    e = ears[0]
    while len(points) > 3:
        ind = points.index(e)
        prev_pred = points[(ind - 2) % length]
        pred = points[(ind - 1) % length]
        succ = points[(ind + 1) % length]
        next_succ = points[(ind + 2) % length]
        if outputtype == "index":
            if rev:
                l = len(all_points) - 1
                edges.append((l - all_points.index(pred), l - all_points.index(succ)))
            else:
                edges.append((all_points.index(pred), all_points.index(succ)))
        elif outputtype == "value":
            edges.append((pred, succ))
        points.remove(e)
        length -= 1
        ears.remove(e)
        if is_ear(points, prev_pred, pred, succ):
            if pred not in ears:
                ears.append(pred)
        else:
            if pred in ears:
                ears.remove(pred)
        if is_ear(points, pred, succ, next_succ):
            if succ not in ears:
                ears.append(succ)
        else:
            if succ in ears:
                ears.remove(succ)
        e = ears[0]
    return edges







