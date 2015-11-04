import inout as io
import triangle as trg
import sys
import time


def main(argv):
    (inputfile, outputfile, outputtype) = io.parse_cmd(argv)
    points = io.read_points(inputfile)
    print("Number of points: {0} \n".format(len(points)))
    start = time.clock()
    (ears, rev) = trg.ears_finding(points)
    edges = trg.ears_clipping(points, ears, outputtype, rev)
    end = time.clock()
    print ("Elapsed time: {0} seconds \n".format(end - start))
    io.save_edges(edges, outputfile, outputtype)


if __name__ == "__main__":
    main(sys.argv[1:])
