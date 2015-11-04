
class Piece():

    def __init__(self, player):
        self.player = player

    def retValue(self):
        raise NotImplementedError
        
class Chick(Piece):

    VAL = 5

    def __init__(self, player):
        super(Chick, self).__init__(player)
        if player == 1:
            self.nextMove = [
                [], [], [],
                [0],[1],[2],
                [3],[4],[5],
                [6],[7],[8],
            ]
            
        else:
            self.nextMove = [
                [3], [4], [5],
                [6], [7], [8],
                [9], [10], [11],
                [], [], [],
            ]

    def retValue(self):
        return Chick.VAL
        
    def __str__(self):
        if self.player == 1:
            return "ひ"
        else:
            return "ヒ"

    def __repr__(self):
        if self.player == 1:
            return "ひ"
        else:
            return "ヒ"

class Hen(Piece):

    VAL = 40

    def __init__(self, player):
        super(Hen, self).__init__(player)
        if player == 1:
            self.nextMove = [
                [1,3],
                [0,2,4],
                [1,5],
                [0,1,4,6],
                [0,1,2,3,5,7],
                [1,2,4,8],
                [3,4,7,9],
                [3,4,5,6,8,10],
                [4,5,7,11],
                [6,7,10],
                [6,7,8,9,11],
                [7,8,10],
            ]
        else:
            self.nextMove = [
                [1,3,4],
                [0,2,3,4,5],
                [1,4,5],
                [0,4,6,7],
                [1,3,5,6,7,8],
                [2,4,7,8],
                [3,7,9,10],
                [4,6,8,9,10,11],
                [5,7,10,11],
                [6,10],
                [7,9,11],
                [8,10],
            ]

    def retValue(self):
        return Hen.VAL

    def __str__(self):
        if self.player == 1:
            return "に"
        else:
            return "ニ"

    def __repr__(self):
        if self.player == 1:
            return "に"
        else:
            return "ニ"

class Elephant(Piece):

    VAL = 30

    def __init__(self, player):
        super(Elephant, self).__init__(player)
        self.nextMove = [
            [4,],
            [3,5,],
            [4,],
            [1,7,],
            [0,6,2,8,],
            [1,7,],
            [4,10,],
            [3,9,5,11,],
            [4,10,],
            [7,],
            [6,8,],
            [7,],
        ]

    def retValue(self):
        return Elephant.VAL

    def __str__(self):
        if self.player == 1:
            return "ぞ"
        else:
            return "ゾ"

    def __repr__(self):
        if self.player == 1:
            return "ぞ"
        else:
            return "ゾ"

class Giraffe(Piece):

    VAL = 30

    def __init__(self, player):
        super(Giraffe, self).__init__(player)
        self.nextMove = [
            [3,1,],
            [0,4,2,],
            [1,5,],
            [6,0,4,],
            [3,7,1,5,],
            [4,8,2,],
            [9,3,7,],
            [6,10,4,8,],
            [7,11,5,],
            [6,10,],
            [9,7,11,],
            [10,8,],
        ]

    def retValue(self):
        return Giraffe.VAL

    def __str__(self):
        if self.player == 1:
            return "き"
        else:
            return "キ"

    def __repr__(self):
        if self.player == 1:
            return "き"
        else:
            return "キ"

class Lion(Piece):

    VAL = 1500

    def __init__(self, player):
        super(Lion, self).__init__(player)
        self.nextMove = [
            [3,1,4,],
            [0,3,4,2,5,],
            [1,4,5,],
            [0,6,1,4,7,],
            [0,3,6,1,7,2,5,8,],
            [1,4,7,2,8,],
            [3,9,4,7,10,],
            [3,6,9,4,10,5,8,11,],
            [4,7,10,5,11,],
            [6,7,10,],
            [6,9,7,8,11,],
            [7,10,8,],
        ]

    def retValue(self):
        return Lion.VAL

    def __str__(self):
        if self.player == 1:
            return "ら"
        else:
            return "ラ"

    def __repr__(self):
        if self.player == 1:
            return "ら"
        else:
            return "ラ"
