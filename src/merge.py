"""Code for merging two sorted lists."""

def merge(x: list[int],y: list[int]) -> list[int]:
    """
    Merge two sorted lists.

    Returns a list that contains all the elements in x and y
    in sorted order.

    >>> merge([1, 2, 4, 6], [1, 3, 4, 5])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    i, j = 0, 0
    z = []  # a new list to copy elements into
    # FIXME: fill out the loop so you merge the lists
    # until one of them is empty
    #print("len(x) = ", len(x), " | ", "len(y) = ", len(y))
    while i < len(x) or j < len(y):
      #print("i = ", i, " | ", "j = ", j)
      if i < len(x) and (j >= len(y) or x[i] <= y[j]):
        z.append(x[i])
        i += 1
      else:
        z.append(y[j])
        j += 1
        
      
      #if len(z) == (len(x) + len(y)):
        #break
    # FIXME: you shouldn't just break here
    # At least one of the lists is empty now. Copy the
    # remainder of the other into z.
    return z

x=[1, 2, 4, 6]
y=[1, 3, 4, 5]
print(merge(x,y))

