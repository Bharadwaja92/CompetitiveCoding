"""
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by 
rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). 
If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

Input: img = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
Output: [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

img = [
    [100,200,100],
    [200,50,200],
    [100,200,100]
    ]
Output: [
    [137,141,137],
    [141,138,141],
    [137,141,137]
    ]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
"""


def get_smoothed_pixel(img, r, c, num_rows, num_cols):
    row_up = max([0, r-1])
    row_down = min([r+1, num_rows-1])
    col_left = max([0, c-1])
    col_right = min([c+1, num_cols-1])
    # print((row_up, col_left), (row_up, col_right), (row_down, col_right), (row_down, col_left))
    window = [[img[i][j] for j in range(col_left, col_right+1)] for i in range(row_up, row_down+1)]
    window_avg = sum([sum(row) for row in window]) // (len(window) * len(window[0]))
    # print(window, window_avg)
    return window_avg



class Solution:

    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        num_rows = len(img[0])
        num_cols = len(img)
        img_smooth = [[0]*num_rows] * num_cols

        for r in range(num_rows):
            smooth_row = []
            for c in range(num_cols):
                smoothed = get_smoothed_pixel(img, r, c, num_rows, num_cols)
                # print(r, '-->', c, '-->', img[r][c], '-->', smoothed)
                smooth_row.append(smoothed)
            # print(smooth_row)
            img_smooth[r] = smooth_row

        return img_smooth


s = Solution()
# img = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]

img = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
print(s.imageSmoother(img))


img = [
    [100,200,100],
    [200,50,200],
    [100,200,100]
    ]
print(s.imageSmoother(img))

