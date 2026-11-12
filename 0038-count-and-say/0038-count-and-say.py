
class Solution:
    def countAndSay(self, n):
        result = "1"

        for i in range(n - 1):
            count = 1
            temp = ""

            for j in range(1, len(result)):
                if result[j] == result[j - 1]:
                    count += 1
                else:
                    temp += str(count) + result[j - 1]
                    count = 1

            temp += str(count) + result[-1]
            result = temp

        return result
