def maximumProduct(self, nums):
        m1 = m2 = m3 = float('-inf')
        k1 = k2 = float('inf')
        for x in nums:
            if x > m1:
                m3 = m2
                m2 = m1
                m1 = x
            elif x > m2:
                m3 = m2
                m2 = x
            elif x > m3:
                m3 = x
            if x < k1:
                k2 = k1
                k1 = x
            elif x < k2:
                k2 = x
        return max(
            m1 * m2 * m3,
            m1 * k1 * k2
        )
