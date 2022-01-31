import ast

from refactor import ReplacementAction, Rule, run


class ReplaceAnonRetVal(Rule):
    def match(self, node):
        assert isinstance(node, ast.Return)
        assert isinstance(node.value, ast.IfExp)
        replacement = [
            ast.Assign(
                targets=[ast.Name(id="output")],
                value=node.value,
                lineno=None,
            ),
            ast.Return(value=ast.Name(id="output")),
        ]
        return ReplacementAction(node, replacement)
        
        
if __name__ == "__main__":
    run(rules=[ReplaceAnonRetVal])
