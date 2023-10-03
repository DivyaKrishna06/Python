class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        def count_chars(word):
            char_count = [0] * 26  # Assuming lowercase English letters only
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            return char_count
        
        # Initialize the universal char count with zeros
        universal_char_count = [0] * 26
        
        for word in words2:
            char_count = count_chars(word)
            for i in range(26):
                universal_char_count[i] = max(universal_char_count[i], char_count[i])
        
        result = []
        for word in words1:
            char_count = count_chars(word)
            is_universal = True
            for i in range(26):
                if char_count[i] < universal_char_count[i]:
                    is_universal = False
                    break
            if is_universal:
                result.append(word)
        
        return result

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
solution = Solution()
output = solution.wordSubsets(words1, words2)
print(output)  # Output: ["facebook", "google", "leetcode"]