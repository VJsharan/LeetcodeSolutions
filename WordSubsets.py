class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnt = Counter()
        for b in words2:
            t = Counter(b)
            for c, v in t.items():
                cnt[c] = max(cnt[c], v)
        ans = []
        for a in words1:
            t = Counter(a)
            if all(t[c] >= v for c, v in cnt.items()):
                ans.append(a)
        return ans
'''it creates a counter for a word, which keeps track of all the times, the letters have appeared in it, then accesses all the words 
from words2 and creates one each using for loop, then traverses through the counter-dict created using c and v (Acting as word and their count,), 
it chooses the maximum of it
then accesses all the words in the given input words and creates their counter, then checks if the 
letters count is alteast bigger than the required count, if its true for all the instances then it appends it
to the ans list as its a subset of the given string 
