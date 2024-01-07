class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def convert(self, counter):
        if self:
            counter += 1
            self.left = counter
            for child in self.children:
                counter = child.convert(counter)
            counter += 1
            self.right = counter
        return counter

    def getRelationships(self):
        relationships = []

        def traverse(node, parent):
            if node:
                relationships.append((node.name, parent))
                for child in node.children:
                    traverse(child, node.name)

        traverse(self, None)
        return relationships


# Demonstration
root = Node('Root')

child1 = Node('Child 1')
root.addChild(child1)

child2 = Node('Child 2')
root.addChild(child2)

child3 = Node('Child 3')
root.addChild(child3)

child4 = Node('Child 4')
child1.addChild(child4)

child5 = Node('Child 5')
child2.addChild(child5)

root.convert(0)
relationships = root.getRelationships()

# Display the relationships
for relationship in relationships:
    print('Parent: ', relationship[1], 'Child: ', relationship[0])