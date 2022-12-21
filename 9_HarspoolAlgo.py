def badCharHeuristic(string, size):
	badChar = [-1]*256
	for i in range(size):
		badChar[ord(string[i])] = i;
	return badChar

def search(txt, pat):
	m = len(pat)
	n = len(txt)
	badChar = badCharHeuristic(pat, m)
	s = 0
	while(s <= n-m):
		j = m-1
		while j>=0 and pat[j] == txt[s+j]:
			j -= 1
		if j<0:
			print("Pattern occur at shift = {}".format(s))
			s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
		else:
			s += max(1, j-badChar[ord(txt[s+j])])

txt = "ABAAABCDABCABACABC"
pat = "ABC"
search(txt, pat)