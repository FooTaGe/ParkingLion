import struct
import numpy as np
import PIL
import scipy
import scipy.misc
import scipy.cluster
def dominantColor(filename):
    NUM_CLUSTERS = 3
    print ('reading image')
    im = PIL.Image.open(filename)
    im = im.resize((50, 50))      # optional, to reduce time
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

    print ('finding clusters')
    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
    print ('cluster centres:\n', codes)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

    index_max = scipy.argmax(counts)                    # find most frequent
    peak =  codes[index_max]
    print('max_val:\n', peak)
    return peak
    #peak = codes[index_max]
    #colour = ''.join(chr(int(c)) for c in peak).encode('hex')
    #print ('most frequent is %s (#%s)' % (peak, colour))

if __name__ == "__main__":
    import sys
    dominantColor(sys.argv[1])

