# Sumit Dutta
# v1.0 4/5/2017
#// your Python code to implement the features could be placed here
#// note that you may use any language, there is no preference towards Python

import re
import sys
import numpy as np

# print sys.argv[1]
logfile = sys.argv[1]

# Feature 1

f1 = open(sys.argv[2], 'w')

# f1.write('testing\n')
mydict = {}
hostlist = []

# logdata = np.genfromtxt(logfile, delimiter=" - - ", skip_header=0, dtype=str, usecols=(0))

# logsize = logdata.shape[0]

flog = open(logfile, 'r')
logdata = flog.readlines()
flog.close()

mydict = {}
hostlist = []

logsize = len(logdata)

for i in range(logsize):
    # print str(logdata[0][0])
    hostname = logdata[i].split(' - - ')[0]
    hostlist.append(hostname)

[sortlist, sort_ind, sort_inv, sort_counts] = np.unique(hostlist, return_index=True, return_inverse=True, return_counts=True)
sortkeys = np.argsort(sort_counts)

output = [hostlist[i] for i in sortkeys[-11:-1]]
output_cts = sortkeys[-11:-1]

for k in range(10):
    f1.write(output[k] + ', ' + str(output_cts[k]) + '\n')

#     if (hostname in hostlist):
#         k = hostlist.index(hostname)
#         mydict[k] = mydict[k] + 1
#     else:
#         # mydict[hostname] = 1
#         hostlist.append(hostname)
#         k = hostlist.index(hostname)
#         mydict[k] = 1

# i = 0
# for (key, value) in sorted(mydict.items(), key=lambda x: x[1]):
#     f1.write(hostlist[key] + ', ' + str(value) + '\n')
#     i = i + 1
#     if (i == 10):
#         break

f1.close()

# Feature 2

f2 = open(sys.argv[3], 'w')

f2.close()

# Feature 3

f3 = open(sys.argv[4], 'w')

f3.close()

# Feature 4

f4 = open(sys.argv[5], 'w')

f4.close()

