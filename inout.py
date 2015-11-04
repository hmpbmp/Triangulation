import sys
import getopt


# Parsing command line arguments
def parse_cmd(argv):
    inputfile = ''
    outputfile = ''
    outputtype = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:t:")
    except getopt.GetoptError:
        print 'Call format: main.py -i <inputfile> -o <outputfile> -t <index|value>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Call format: main.py -i <inputfile> -o <outputfile> -t <index|value>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-t", "--otype"):
            outputtype = arg
    if outputtype != "index" and outputtype != "value":
        print 'Call format: main.py -i <inputfile> -o <outputfile> -t <index|value>'
        sys.exit(2)
    print 'Input file is ', inputfile
    print 'Output file is ', outputfile
    print 'Output type is', outputtype
    return inputfile, outputfile, outputtype


# Read polygon from file as list of points represented by tuples
def read_points(inputfile):
    points = []
    file_in = open(inputfile, "r")
    for line in file_in:
        coords = line.split()
        if len(coords) != 2:
            print 'Wrong input file format'
            sys.exit(3)
        points.append((int(coords[0]), int(coords[1])))
    return points


# Save list of edges
def save_edges(edges, outputfile, outputtype):
    file_put = open(outputfile, "w")
    for e in edges:
        if outputtype == "index":
            file_put.write("{0} --- {1} \n".format(e[0], e[1]))
        else:
            file_put.write("{0} {1} --- {2} {3}\n".format(e[0][0], e[0][1], e[1][0], e[1][1]))


