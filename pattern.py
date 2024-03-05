# ========= Task 1 ===========
# Code below outputs a star pattern, using an ifelse statement and a single for loop:

# Sets the maximum number of stars in the middle row.
mid_stars = 5

# Iterates through a range double the size of mid_stars, minus -1 to avoid duplication.
for i in range(1, (mid_stars * 2)):

# The first 5 lines increases in star count.
# Checks whether star number is less than or equal to max star number in the pattern's middle.
# If i is less than or equal to, the star count is equal to the current iteration.
    if i <= mid_stars:
        stars = i

# The last 5 lines decreases in star count.
# If i is not less than or equal to the star count, i is subtracted to get the decreasing star count.
    else:
        stars = (mid_stars *2) - i

# String multiplication at the end visualises the correct star pattern.
    print('*' * stars)