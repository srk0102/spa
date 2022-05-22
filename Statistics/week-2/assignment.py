def avg(l):
    return sum(l)/float(len(l))

def distance_btw_clusters(p, q):
    return abs(p - q)

def initialize(values, k):
    if k < len(values):
        global groups
        groups = [ [x, [x], values.index(x)] for x in values[0:k] ]
        groups.sort()
        for value in values[k:len(values)]:
            group = findGroup(value, groups)
            group[1].append(value)

def findGroup(p, l):
    if len(l) == 1:
        return l[0]
    midpoint = int((len(l)-1) / 2)
    d1 = distance_btw_clusters(p, l[midpoint][0])
    d2 = distance_btw_clusters(p, l[midpoint + 1][0])
    if d1 < d2:
        return findGroup(p, l[0:midpoint + 1])

    return findGroup(p, l[midpoint + 1:len(l)])

def recalculate_centroids():
    for group in groups:
        group[0] = avg(group[1])

def rebalance():
    recalculate_centroids()
    point_moved = False
    for group in groups:
        mean = group[0]
        values = group[1]
        for value in values:
            new_group = findGroup(value, groups)
            if new_group[0] != mean:
                point_moved = True
                values.remove(value)
                new_group[1].append(value)
    return point_moved

def groups():
    return groups

def converge(output_fn=None):
    iteration_num = 1
    output_fn(iteration_num)
    while (rebalance()):
        iteration_num += 1
        if output_fn:
            output_fn(iteration_num)
    output_fn(iteration_num + 1)
def output(iteration_num):
    # print as shown in sample output
    print("Iteration %d" % iteration_num)
    clusters = sorted(groups, key=lambda x : x[2])
    for cluster in clusters:
        print("%d %s" % (cluster[2], cluster[1]))
    print("\n")

def write_results(out_file):
    with open(out_file, 'w+') as file:
        for group in groups:
            for item in group[1]:
                file.write("Point %s in cluster %d \n" % (item, group[2]))

def main():
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")
    k = int(input("Enter the number of clusters: "))
    print("\n")

    with open(input_file) as file:
        nums = [float(line.strip()) for line in file]
    initialize(nums, k)            # creates k groups
    converge(output)               # shuffles until convergence
    write_results(output_file)     # creates required out file

if __name__ == "__main__":
    print("Course Name :- \n")
    print("NAME:- \n")
    print( "PROGRAMMING ASSIGNMENT #2 \n")
    main()