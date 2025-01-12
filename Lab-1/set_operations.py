# Set Operations in Python

# Creating a set from a list (removes duplicates)
shapes = ['circle', 'square', 'triangle', 'circle']
setOfShapes = set(shapes)
print(setOfShapes)  # Output: {'circle', 'square', 'triangle'}

# Adding an element to the set
setOfShapes.add('polygon')
print(setOfShapes)  # Output: {'circle', 'square', 'triangle', 'polygon'}

# Checking membership in the set
print('circle' in setOfShapes)  # Output: True
print('rhombus' in setOfShapes)  # Output: False

# Creating another set from a list
favoriteShapes = ['circle', 'triangle', 'hexagon']
setOfFavoriteShapes = set(favoriteShapes)

# Set Difference: Elements in setOfShapes but not in setOfFavoriteShapes
print(setOfShapes - setOfFavoriteShapes)  # Output: {'square', 'polygon'}

# Set Intersection: Common elements between setOfShapes and setOfFavoriteShapes
print(setOfShapes & setOfFavoriteShapes)  # Output: {'circle', 'triangle'}

# Set Union: All unique elements from both sets
print(setOfShapes | setOfFavoriteShapes)  # Output: {'circle', 'square', 'triangle', 'polygon', 'hexagon'}
