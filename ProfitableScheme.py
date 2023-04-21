def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        G, P = n, minProfit
        knapsack = [[0] * (G + 1) for i in range(P + 1)]
        knapsack[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G-g, -1, -1):
                    print(knapsack)
                    knapsack[min(i + p, P)][j + g] += knapsack[i][j]
        
        return sum(knapsack[P]) % (10**9 + 7)

      # knapsack problem
