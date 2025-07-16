class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_map = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            fragments = domain.split('.')

            for i in range(len(fragments)):
                subdomain = ".".join(fragments[i:])
                count_map[subdomain] += count

        return [f"{cnt} {dom}" for dom, cnt in count_map.items()]