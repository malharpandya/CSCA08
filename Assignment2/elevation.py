"""Assignment 2 functions."""

from typing import List


THREE_BY_THREE = [[1, 2, 1],
                  [4, 6, 5],
                  [7, 8, 9]]

FOUR_BY_FOUR = [[1, 2, 6, 5],
                [4, 5, 3, 2],
                [7, 9, 8, 1],
                [1, 2, 1, 4]]

UNIQUE_3X3 = [[1, 2, 3],
              [9, 8, 7],
              [4, 5, 6]]

UNIQUE_4X4 = [[10, 2, 3, 30],
              [9, 8, 7, 11],
              [4, 5, 6, 12],
              [13, 14, 15, 16]]


def compare_elevations_within_row(elevation_map: List[List[int]], map_row: int,
                                  level: int) -> List[int]:
    """Return a new list containing the three counts: the number of
    elevations from row number map_row of elevation map elevation_map
    that are less than, equal to, and greater than elevation level.

    Precondition: elevation_map is a valid elevation map.
                  0 <= map_row < len(elevation_map).

    >>> compare_elevations_within_row(THREE_BY_THREE, 1, 5)
    [1, 1, 1]
    >>> compare_elevations_within_row(FOUR_BY_FOUR, 1, 2)
    [0, 1, 3]

    """
    less_than, equal_to, grt_than = 0, 0, 0
    for element in elevation_map[map_row]:
        if element < level:
            less_than = less_than + 1
        elif element == level:
            equal_to = equal_to + 1
        else:
            grt_than = grt_than + 1
    return [less_than, equal_to, grt_than]


def update_elevation(elevation_map: List[List[int]], start: List[int],
                     stop: List[int], delta: int) -> None:
    """Modify elevation map so that the elevation of each
    cell between cells start and stop, inclusive, changes by amount
    delta.

    Precondition: elevation_map is a valid elevation map.
                  start and stop are valid cells in elevation_map.
                  start and stop are in the same row or column or both.
                  If start and stop are in the same row,
                      start's column <=  stop's column.
                  If start and stop are in the same column,
                      start's row <=  stop's row.
                  elevation_map[i, j] + delta >= 1
                      for each cell [i, j] that will change.

    >>> THREE_BY_THREE_COPY = [[1, 2, 1],
    ...                        [4, 6, 5],
    ...                        [7, 8, 9]]
    >>> update_elevation(THREE_BY_THREE_COPY, [1, 0], [1, 1], -2)
    >>> THREE_BY_THREE_COPY
    [[1, 2, 1], [2, 4, 5], [7, 8, 9]]
    >>> FOUR_BY_FOUR_COPY = [[1, 2, 6, 5],
    ...                      [4, 5, 3, 2],
    ...                      [7, 9, 8, 1],
    ...                      [1, 2, 1, 4]]
    >>> update_elevation(FOUR_BY_FOUR_COPY, [1, 2], [3, 2], 1)
    >>> FOUR_BY_FOUR_COPY
    [[1, 2, 6, 5], [4, 5, 4, 2], [7, 9, 9, 1], [1, 2, 2, 4]]

    """
    
    row_start, col_start = start[0], start[1]
    row_stop, col_stop = stop[0], stop[1]
    if row_start == row_stop:
        for i in range(col_start, col_stop + 1):
            elevation_map[row_stop][i] = elevation_map[row_stop][i] + delta
    else:
        for i in range(row_start, row_stop + 1):
            elevation_map[i][col_stop] = elevation_map[i][col_stop] + delta

def get_average_elevation(elevation_map: List[List[int]]) -> float:
    """Return the average elevation across all cells in the elevation map
    elevation_map.

    Precondition: elevation_map is a valid elevation map.

    >>> get_average_elevation(UNIQUE_3X3)
    5.0
    >>> get_average_elevation(FOUR_BY_FOUR)
    3.8125
    """
    
    count = 0
    size = len(elevation_map)
    for row in range(size):
        for col in range(size):
            count = count + elevation_map[row][col]
    return count / size ** 2


def find_peak(elevation_map: List[List[int]]) -> List[int]:
    """Return the cell that is the highest point in the elevation map
    elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  Every elevation value in elevation_map is unique.

    >>> find_peak(UNIQUE_3X3)
    [1, 0]
    >>> find_peak(UNIQUE_4X4)
    [0, 3]
    """
    
    peak_location = []
    init_pos = elevation_map[0][0]
    size = len(elevation_map)
    for row in range(size):
        for col in range(size):    
            if elevation_map[row][col] > init_pos:
                init_pos = elevation_map[row][col]
                peak_location = [row, col]
    return peak_location

def is_sink(elevation_map: List[List[int]], cell: List[int]) -> bool:
    """Return True if and only if cell exists in the elevation map
    elevation_map and cell is a sink.

    Precondition: elevation_map is a valid elevation map.
                  cell is a 2-element list.

    >>> is_sink(THREE_BY_THREE, [0, 5])
    False
    >>> is_sink(THREE_BY_THREE, [0, 2])
    True
    >>> is_sink(THREE_BY_THREE, [1, 1])
    False
    >>> is_sink(FOUR_BY_FOUR, [2, 3])
    True
    >>> is_sink(FOUR_BY_FOUR, [3, 2])
    True
    >>> is_sink(FOUR_BY_FOUR, [1, 3])
    False
    """

    size = len(elevation_map)
    i, j = cell[0], cell[1]
    if i > size or j > size:
        return False
    for row in range(max(i - 1, 0), min(i + 2, size)):
        for col in range(max(j - 1, 0), min(j + 2, size)):    
            if elevation_map[row][col] < elevation_map[i][j]:
                return False
    return True
        
    


def find_local_sink(elevation_map: List[List[int]],
                    cell: List[int]) -> List[int]:
    """Return the local sink of cell cell in elevation map elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  elevation_map contains no duplicate elevation values.
                  cell is a valid cell in elevation_map.

    >>> find_local_sink(UNIQUE_3X3, [1, 1])
    [0, 0]
    >>> find_local_sink(UNIQUE_3X3, [2, 0])
    [2, 0]
    >>> find_local_sink(UNIQUE_4X4, [1, 3])
    [0, 2]
    >>> find_local_sink(UNIQUE_4X4, [2, 2])
    [2, 1]
    """
    
    size = len(elevation_map)
    i, j = cell[0], cell[1]
    value = elevation_map[i][j]
    for row in range(max(i - 1, 0), min(i + 2, size)):
        for col in range(max(j - 1, 0), min(j + 2, size)):
            if elevation_map[row][col] <= value:
                value = elevation_map[row][col]
                sink_row, sink_col = row, col
    return [sink_row, sink_col]


def can_hike_to(elevation_map: List[List[int]], start: List[int],
                dest: List[int], supplies: int) -> bool:
    """Return True if and only if a hiker can go from start to dest in
    elevation_map without running out of supplies.

    Precondition: elevation_map is a valid elevation map.
                  start and dest are valid cells in elevation_map.
                  dest is North-West of start.
                  supplies >= 0

    >>> map = [[1, 6, 5, 6],
    ...        [2, 5, 6, 8],
    ...        [7, 2, 8, 1],
    ...        [4, 4, 7, 3]]
    >>> can_hike_to(map, [3, 3], [2, 2], 10)
    True
    >>> can_hike_to(map, [3, 3], [2, 2], 8)
    False
    >>> can_hike_to(map, [3, 3], [3, 0], 7)
    True
    >>> can_hike_to(map, [3, 3], [3, 0], 6)
    False
    >>> can_hike_to(map, [3, 3], [0, 0], 18)
    True
    >>> can_hike_to(map, [3, 3], [0, 0], 17)
    False

    """
    
    i, j = start[0], start[1]
    while i > dest[0] and j > dest[1]:
        up, left = abs(elevation_map[i - 1][j]), abs(elevation_map[i][j - 1])
        if up <= left:
            dif, i = abs(elevation_map[i - 1][j] - elevation_map[i][j]), i - 1
        else:
            dif, j = abs(elevation_map[i][j - 1] - elevation_map[i][j]), j - 1
        supplies = supplies - dif
    if i == dest[0]:
        while j != dest[1]:
            dif, j = abs(elevation_map[i][j - 1] - elevation_map[i][j]), j - 1
            supplies = supplies - dif
    elif j == dest[1]:
        while i != dest[0]:
            dif, i = abs(elevation_map[i - 1][j] - elevation_map[i][j]), i - 1
            supplies = supplies - dif
    return supplies >= 0


### HELPER FUNCTION FOR get_lower_resolution.
### Not called if the square matrix is even.
### It replicates the bottom row and right column to make elevation_map 
### an even square matrix with the same average for each 2 x 2 sub-matrix.
def map_modify(elevation_map: List[List[int]]) -> List[List[int]]:
    """Modify elevation_map if len(elevation_map) is odd, by adding  a 
    replicate of the bottom and right border and adding element 
    elvation_map[i][j] to the bottom right corner of modified elevation_map.
    
    Precondition: elevation_map is a valid elevation map.
    
    >>> case_1 = [[1, 6, 5, 6],
    ...          [2, 5, 6, 8],
    ...          [7, 2, 8, 1],
    ...          [4, 4, 7, 3]]
    >>> map_modify(case_1)
    >>> case_1
    [[1, 6, 5, 6], [2, 5, 6, 8], [7, 2, 8, 1], [4, 4, 7, 3]]
    >>> case_2 = [[7, 9, 1],
    ...       [4, 2, 1],
    ...       [3, 2, 3]]
    >>> map_modify(case_2)
    >>> case_2
    [[7, 9, 1, 1], [4, 2, 1, 1], [3, 2, 3, 3], [3, 2, 3, 3]]
    
    """
    
    size = len(elevation_map)
    if size % 2 != 0:
        for row in range(size):
            elevation_map[row].append(elevation_map[row][size - 1])
        elevation_map.append(elevation_map[size - 1])
    
def get_lower_resolution(elevation_map: List[List[int]]) -> List[List[int]]:
    """Return a new elevation map, which is constructed from the values
    of elevation_map by decreasing the number of elevation points
    within it.

    Precondition: elevation_map is a valid elevation map.

    >>> get_lower_resolution(
    ...     [[1, 6, 5, 6],
    ...      [2, 5, 6, 8],
    ...      [7, 2, 8, 1],
    ...      [4, 4, 7, 3]])
    [[3, 6], [4, 4]]
    >>> get_lower_resolution(
    ...     [[7, 9, 1],
    ...      [4, 2, 1],
    ...      [3, 2, 3]])
    [[5, 1], [2, 3]]

    """
    
    map_modify(elevation_map)
    size = len(elevation_map)
    low_res = []
    for row in range(0, size, 2):
        low_res.append([])
        for col in range(0, size, 2):
            sum_values = (elevation_map[row][col]
                          + elevation_map[row][col + 1]
                          + elevation_map[row + 1][col]
                          + elevation_map[row + 1][col + 1]) / 4
            low_res[int(row/2)].append(int(sum_values))
    return low_res