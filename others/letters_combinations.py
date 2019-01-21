def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    map_ = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz'
    }
    result = []
    def make_combinations(i, cur):
        if len(cur) == len(digits):
            print cur
            return

        for ch in map_[digits[i]]:
            cur.append(ch)
            make_combinations(i+1, cur)
            cur.pop()
    
    make_combinations(0, [])
    return result
letterCombinations("234")