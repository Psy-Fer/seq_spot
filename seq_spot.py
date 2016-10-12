from matplotlib import pyplot as plt

s=["AATTCGCGCTTACGCTAGGCTAGCTAGGCTCGATTCGAGGCTCGGGATCGATCGGTACGAGGTACGTACTGACTGACT",
  "ACTGGGCTATGCGGGATATATATATCGCGACTGACATGCATGCTAGGCGCGCTATAATCGGCGCATATAGCTAGCTAG",
  "ACTGACGTACGTAGCTAGCTAGGCTATATAGCGCGCATATCGCGAGTATACGTAGCTAGCTGACTGGCGATATATCGA",
  "ACGTGAGCTGATGTGTGAGTACTATATGCGATAGCTACGTAGCTGATCAGCTAGCGATTAGCGCTATAGCTAGCTATG",
  "ACTGACTGATATCGATCGGCGCGCGTATAGCGCTATAGCGATCGATGTGACTGATCGATATATATCGGCTATAGCGAT",
  "TTGCTAGCTAGATCGTGACTGACTGTGACTGACTGACTGTACGACTGACTGTGACTATCGATACGCTAGATCGACTAT",
  "GGCTACGTACGATGCTAGCTAGCTGGGGGGTACGATCGTGACTGACTAAATCGATATATATATAGCTGACTGACTGAT",
  "CCCCGCTAGCTATACGTACGCTAGCTAGCTAGCTGCGCGCGATGCGATCGATCGACTGTGACTGACTGACGTGACTGC"]

dic = {"C": (255, 0, 0),
       "G": (0 , 255 , 0),
       "A": (0, 0, 255),
       "T": (255, 255, 0)}

##### ^^^ Not used  #####

dic2 = {"A": 1, "C": 2, "G": 3, "T": 4}

tot = 10000

fasta = "psyfer_seq.fasta"
L = []
count = 0
with open(fasta, "rb") as fa:
    for line in fa:
        if count > 10000:
            break
        if line[0] == ">":
            continue
        else:
            K = []
            for z in line.rstrip():
                K.append(dic2[z])
            L.append(K + [-1] * (tot - len(K)))
            #L.append(K)
        count += 1

#print L
im_filename = "test8.png"
fig = plt.figure(1)
plt.imshow(L, interpolation='nearest')
plt.grid(True)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
#plt.show()
plt.savefig(im_filename,format="png", bbox_inches='tight', pad_inches=0)

