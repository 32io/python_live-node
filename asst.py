import ast
tree = ast.parse("print('hello world')")

for node in ast.walk(tree):
    print(node)
    print(node.__dict__)
    print("children: " + str([x for x in ast.iter_child_nodes(node)]) + "\\n")
print(ast.dump(tree))