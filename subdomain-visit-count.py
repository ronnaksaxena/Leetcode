class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        visits = collections.defaultdict(int)
        
        for dom in cpdomains:
            # to get num part1.part2.partx
            freq, parts = dom.split(' ')
            ds = parts.split('.')
            s = ''
            # Wanted to build domains backwards
            for d in reversed(ds):
                if not s:
                    s = d
                    visits[s]  += int(freq)
                else:
                    s = d + '.' + s
                    visits[s] += int(freq)
                    
        output= []
        for dom, freq in visits.items():
            output.append('{} {}'.format(freq, dom))
            
        return output
                
            
        
