class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""

		dictWords = {};
		dictPattern = {};
		words = str.split();

		if(len(words) != len(pattern)):
			return False;

		for i in range(len(pattern)):
			if(pattern[i] not in dictPattern and words[i] not in dictWords):
				dictPattern[pattern[i]] = words[i];
				dictWords[words[i]] = pattern[i];

			if(pattern[i] in dictPattern and words[i] in dictWords):
				if(dictPattern[pattern[i]] != words[i] or dictWords[words[i]] != pattern[i]):
					return False;
			else:
				return False;

		#print(dictWords);
		#print(dictPattern);
		return True;

sol = Solution();

pattern = "abba";
str = "a c b a";

print(sol.wordPattern(pattern, str));

