class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        count = 0
        dictionary = set()
        for elem in emails:
            abc = elem.split("@")
            abc[0] = abc[0].replace(".","")
            abc[0] = abc[0].split("+")[0]
            i = "".join(abc)
            if i not in dictionary:
                dictionary.add(i)
                count +=1
        return count
data = Solution()
input = ["test.email+alex@leet.code.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(data.numUniqueEmails(input))