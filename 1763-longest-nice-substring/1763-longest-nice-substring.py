class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        N = len(s)
        maxlen = 0
        start = 0
        for i in range(N):
            seen = set()
            missing = 0
            for j in range(i, N):
			# if we haven't seen this "type", add it into the seen set
                if s[j] not in seen: 
                    seen.add(s[j])
					# since this is the first time we see this "type" of character
					# we check if the other half has already been seen before
                    if (s[j].lower() not in seen) or (s[j].upper() not in seen):
                        missing += 1 # we haven't seen the other half yet, so adding 1 to the missing type
                    else: # otherwise we know this character will compensate the other half which we pushed earlier into the set, so we subtract missing "type" by 1
                        missing -= 1
                if missing == 0 and (j - i + 1) > maxlen:
                    maxlen = j - i + 1
                    start = i
        return s[start:(start + maxlen)]