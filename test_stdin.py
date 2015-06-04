#Write your code here

import sys
data = sys.stdin.readlines()
print "Counted", len(data), "lines."
(N,K) = map(int, data[0].split())
print N,K
ini_conf = map(int,data[1].split())
final_conf = map(int,data[2].split())
