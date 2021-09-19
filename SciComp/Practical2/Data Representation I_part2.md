### Exercise: assemble a directed acyclic graph with the numbers 1-12 by strict divisibility: an edge from A to B if B/A is prime. There are no directed cycles, but some nodes do have multiple paths to them. (These form cycles if you ignore the direction.) Which ones? Explain how to decide if a number will have multiple paths to it.


                  7    5 ->- 10       8
                   ↖  ↗     ↗       ↗
             11 -<-  1  ->- 2  ->- 4
                      ↘      ↘      ↘
                  9 -<- 3 ->- 6 ->-  12


6, 10, 12 - Multiple paths due to the fact that they are devisable by two prime numbers


### Exercise: Identify several maximal spanning trees in the divisibility graph from the previous exercise.

1 -> 2 -> 4 -> 8

1 -> 2 -> 4 -> 12

1 -> 3 -> 6 -> 12

### Exercise: model acquaintance using a graph (vertices are people, an edge between A and B means A knows B). Model it with a directed graph. How are these different?

The previous graph allowed only oneway edges, and acquaintance assumes
that A and B can know each other, thus cycles are possible.

### Exercise: this doesn't mean the file was transferred correctly; why not?

The pieces can get scrambled.

### Exercise: do the same for files with "cat" and "cat2" instead of "hi" and "hi2"

$ echo cat > testfile; echo cat2 > testfile2

$ md5sum testfile testfile2
54b8617eca0e54c7d3c8e6732c6b687a *testfile
4307ab44204de40235bad8c66cce0ae9 *testfile2

$ sha1sum testfile testfile2
8f6abfbac8c81b55f9005f7ec09e32d29e40eb40 *testfile
f476b8741936d51309437ffc5c87081c7b24ffb1 *testfile2

$ sha512sum testfile testfile2 # sha2, hash size is 512bit
644c7b649d31fc3c432534fb80d71a3a5e2b3eb65e737eb15c6e6af96e40c8ee3dcb55fd172e263783e62f8d94f5c99e12a016d581b860700640e45c9c1b87b3 *testfile
84c308d32247eb3b590ff27b47d5018551dd6ad3e696b6d61b1e70fed7570522812a2c3353e93db38728f4a10de5156996b144d2b150f1ffe92ba7a301b5bfe2 *testfile2

$ b2sum testfile testfile2 # blake2
0247169dd9d258599e4a4327067f74f3dbd7db0e6d623954212738e62c233b410141a1eab4130073b99a8959e3d52f70da7402ae8d94ca6333126ec3b4e0bca7 *testfile
48d92c152ff4c58a948d75f7aaba6ccaf00f8f9beb78e3399fe0f325e758af657c07eb2d83a753f3fe16074b149f46390abce8673c7477f75aae99427c9defa7 *testfile2

###Exercise: implement the Caesar cipher in python, which advances each letter of 'M' by 'SEC = n': enc(1, "a") = "b", etc.
[here](DRI_caesar.py)

