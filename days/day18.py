from typing import List, NewType
def solve_naive(data: List[str]):
    first = 0
    for expr in data:
        paren_stack = []
        acc = 0
        op = None
        for c in expr:
            if c.isspace():
                continue
            elif c == "+":
                op = True
            elif c == "*":
                op = False
            elif c == "(":
                paren_stack.append((acc, op))
                acc = 0
                op = None
            elif c == ")":
                a, o = paren_stack.pop()
                if o is None:
                    pass
                elif o:
                    acc = a + acc
                else:
                    acc = a * acc
                op = None
            else:
                if op is None:
                    acc = int(c)
                elif op:
                    acc = acc + int(c)
                else:
                    acc = acc * int(c)
                op = None
        
        first += acc

    second = 0
    # cba to actually make a proper parser. here lies the ruins


    # rules = {
    #     "NUM": [["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"]],
    #     "ADD": [["NUM"], ["ADD", "+", "ADD"], ["(", "PROD", ")"]],
    #     "PROD": [["ADD", "*", "ADD"], ["ADD"], ["(", "PROD", ")"]],
    # }
    # actions = {
    #     "NUM": lambda n: int(n),
    #     "ADD": lambda *a: a[0] if len(a) == 1 else (a[1] if a[0] == "(" else a[0] + a[2]),
    #     "PROD": lambda *a: a[0] if len(a) == 1 else (a[1] if a[0] == "(" else a[0] * a[2]),
    # }
    # def match_rule(rule, tokens):
    #     for option in rules[rule]:
    #         new_tokens = tokens.copy()
    #         matches = []
    #         total_length = 0
    #         try:
    #             for part in option:
    #                 if part.isupper():
    #                     match, length = match_rule(part, new_tokens)
    #                     matches.append(match)
    #                     new_tokens = new_tokens[length:]
    #                     total_length += length
    #                 else:
    #                     if new_tokens[0] == part:
    #                         matches.append(new_tokens.pop(0))
    #                         total_length += 1
    #                     else:
    #                         raise SyntaxError
    #         except SyntaxError:
    #             ...
    #         else:
    #             return actions[rule](*matches), total_length
    #     raise SyntaxError

    # for expr in data:
    #     paren_stack = []
    #     acc = 0
    #     op = None
    #     tokens = []
    #     for c in expr:
    #         if c.isspace(): continue
    #         tokens.append(c)
    #     result, _ = match_rule("PROD", tokens)
    #     second += result


    # weep, for I shall cheat
    import ast
    class MyNodeTransformer(ast.NodeTransformer):
        def visit_BinOp(self, node: ast.BinOp):
            if isinstance(node.op, ast.Mult):
                return ast.BinOp(self.visit(node.left), ast.Add(), self.visit(node.right))
            elif isinstance(node.op, ast.Add):
                return ast.BinOp(self.visit(node.left), ast.Mult(), self.visit(node.right))
            else:
                return node
    second = sum([eval(compile(ast.fix_missing_locations(MyNodeTransformer().visit(ast.parse(expr.replace("+", "z").replace("*", "+").replace("z", "*"), "<expr>", "eval"))), "<expr>", "eval")) for expr in data])

    return first, second


implementations = (solve_naive,)
