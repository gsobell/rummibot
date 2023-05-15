# implement game class to store table, hand, pool:
# class Game:
#     def __init__(self):
#         self.pool = self.pool_gen()
#         self.hand = self.hand_gen()
#         self.table = []
#
#     def hand_gen(self):
#         hand = []
#         for i in range(1, 14):
#             k = randrange(len(self.pool))
#             hand.append(self.pool.pop(k))
#         return hand
#
#     def pool_gen(self):
#         tiles = []
#         for i in range(53):
#             tiles.append(i)
#             tiles.append(i)
#         return tiles
