class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        black = "aceg"
        white = "bdfh"

        if coordinates[0] in black:
            if int(coordinates[1]) % 2 != 0:
                return False
            else:
                return True
        else:
            if int(coordinates[1]) % 2 == 0:
                return False
            else:
                return True
