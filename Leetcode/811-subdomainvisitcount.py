class Solution:
    def subdomainVisits(self, cpdomains):
        storage = {}
        for x in cpdomains:
            [num, domain] = x.split(" ")
            num = int(num)
            while(domain):
                if domain in storage:
                    storage[domain] += num
                else:
                    storage[domain] = num
                
                if(domain.find(".") == -1):
                    break
                domain = domain[domain.find(".")+1:]
        
        ans = []
        for domain, num in storage.items():
            ans.append(str(num) + " " + domain)
        return ans

sol = Solution()
x = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(sol.subdomainVisits(x))
