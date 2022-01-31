import ast

from refactor import ReplacementAction, Rule, run


class ReplaceTernaryWalrusAssignment(Rule):
    def match(self, node):
        assert isinstance(node, ast.Return)
        assert isinstance(node.value, ast.IfExp)
        assert isinstance(node.value.test.left, ast.NamedExpr)
        replacement = [
            ast.Assign(
                targets=[node.value.test.left.target],
                value=node.value.test.left.value,
                lineno=None,
            ),
            ast.Return(
                value=ast.IfExp(
                    test=ast.Compare(
                        left=node.value.test.left.target,
                        ops=node.value.test.ops,
                        comparators=node.value.test.comparators,
                    ),
                    body=node.value.body,
                    orelse=node.value.orelse,
                )
            ),
        ]
        return ReplacementAction(node, replacement)


if __name__ == "__main__":
    run(rules=[ReplaceTernaryWalrusAssignment])
