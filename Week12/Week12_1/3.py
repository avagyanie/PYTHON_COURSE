"""
Պետք է սարքենք իքս-նոլիկ խաղը (Tic tak toe) .
Ուրեմն կառուցվածքը սա է լինելու․
    Board class
    Player class
    Humanplayer class
    Computer player class
    Move class
    Game class    ,որ և ամեն բան իրա մեջ կներառի։
Այս կլասնները ոնց կուզեք սարքեք ու վերջում ինձ խաղ տվեք։
Պայտոն կոդը ռան անելուց հետո պետք է տպի դատարկ 3x3 վրա boardը։
Ես կընտրեն՝ որ դաշտում եմ x դնում, համակարգիչը՝ o
Այդպես շարունակ մինչև կրվեմ, կրեմ կամ հավասար խաղ ստացվի։
"""


class Board:
    def __init__(self) -> None:
        pass
    def board(self):
        self.lst = [[" " for i in range(3)] for j in range(3)]
        return self.lst

class Player:
    def __init__(self, name) -> None:
        self.name = name
        print(f"Hello {self.name}! Let's play!")
        print("Now you can select an empty square and click there.")

class Humanplayer:
    def __init__(self) -> None:
        pass

class Computer_player:
    def __init__(self) -> None:
        pass

class Move:
    def __init__(self) -> None:
        pass

class Game:
    def __init__(Board) -> None:
        pass

x = Board()
print(x.board())
y = Game()
