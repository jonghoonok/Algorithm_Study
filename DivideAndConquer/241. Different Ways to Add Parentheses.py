class Solution:
    operators = ['+', '-', '*']

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    temp = 0
                    if op == '+': temp = l+r
                    elif op == '-': temp = l-r
                    else: temp = l*r
                    results.append(temp)
            return results

        results = []
        for i, v in enumerate(expression):
            if v in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                results.extend(compute(left, right, v))
        return results