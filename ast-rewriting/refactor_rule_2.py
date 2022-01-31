import ast

from refactor import ReplacementAction, Rule, run


class ReplaceTernaryAssignment(Rule):
    def match(self, node):
        assert isinstance(node, ast.Assign)
        assert isinstance(node.value, ast.IfExp)
        replacement = ast.If(
            test=ast.Compare(
                left=node.value.test.left,
                ops=node.value.test.ops,
                comparators=node.value.test.comparators,
            ),
            body=[
                ast.Assign(
                    targets=node.targets,
                    value=node.value.body,
                    lineno=None,
                )
            ],
            orelse=[
                ast.Assign(
                    targets=node.targets,
                    value=node.value.orelse,
                    lineno=None,
                )
            ],
        )
        return ReplacementAction(node, replacement)


if __name__ == "__main__":
    run(rules=[ReplaceTernaryAssignment])
