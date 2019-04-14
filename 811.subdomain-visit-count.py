class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_visits = {}

        for cpd in cpdomains:
            num, domain = cpd.split(" ")
            num = int(num)
            splitted_domain = domain.split(".")
            subdomains = ['.'.join(splitted_domain[i:]) for i in range(len(splitted_domain))]
            for subdomain in subdomains:
                if subdomain in domain_visits:
                    domain_visits[subdomain] += num
                else:
                    domain_visits[subdomain] = num

        return [' '.join([str(val), key]) for key, val in domain_visits.items()]