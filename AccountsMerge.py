def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
        people = defaultdict(list)
        
        for account in accounts:
            name = account[0]
            emails = set()
            for i in range(1, len(account)):
                email = account[i]
                emails.add(email)
            
            match = False
            for i in range(len(people[name])):
                reg_email = people[name][i]
                if len(emails.intersection(reg_email)) != 0:
                    emails.update(reg_email)
                    reg_email.clear()
            people[name].append(emails)
        
        print(people)   
        
        res = []
        for k in people.keys():
            for emails in people[k]:
                if not emails:
                    continue
                l = sorted(list(emails))
                res.append([k] + l)
        
        return res
