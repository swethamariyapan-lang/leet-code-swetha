
class Solution:
    def floodFill(self, image, sr, sc, color):
        old_color = image[sr][sc]

        if old_color == color:
            return image

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= len(image) or c >= len(image[0]) or
                image[r][c] != old_color):
                return

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
