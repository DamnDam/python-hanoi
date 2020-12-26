"""
Hanoi Towers
© DT 12/2020
"""

import sys
import argparse

class Hanoi():
    stacks = {
        'A': [],
        'B': [],
        'C': []
    }

    def __str__(self):
        def print_stack(stack):
            string = f"{stack}♖ "
            for i in self.stacks[stack][1:]:
                string += f"[{i}]"
            return string

        return f"{print_stack('A')}\n{print_stack('B')}\n{print_stack('C')}"

    def _valid_ref(self, *args):
        for ref in args:
            if not ref in self.stacks.keys():
                raise IndexError(f"⛔ Inconnu: '{ref}' ⛔\nUtiliser 'A' 'B' ou 'C'")

    def __init__(self, size, source='A'):
        self._valid_ref(source)
        for i in self.stacks.keys():
            self.stacks[i] = [sys.maxsize]
        self.source = source
        self.stacks[source] = [sys.maxsize, *list(range(size, 0, -1))]
        self.count = 1

    def move(self, source, dest, verbose=False):
        self._valid_ref(source, dest)
        if verbose:
            print(f"{self.count:#03} {source}♖ -> {dest}♖")
        if len(self.stacks[source]) == 1 or self.stacks[source][-1] >= self.stacks[dest][-1]:
            raise RuntimeError("⛔ Impossible ⛔")
        self.count +=1
        v = self.stacks[source].pop()
        self.stacks[dest].append(v)

    def solve(self, source, dest, third=None, size=None):
        self._valid_ref(source, dest)
        if size == 0: return
        if size == None: size = len(self.stacks[self.source]) -1
        if not third:
            for k in self.stacks.keys():
                if not k in [source, dest]:
                    third = k
                    break
        self.solve(source, third, dest, size-1)
        self.move(source, dest, verbose=True)
        self.solve(third, dest, source, size-1)

def play():
    print("♖♖ Tours de Hanoi ♖♖")
    size = int(input("Taille de tour> "))
    game = Hanoi(size)
    while True:
        print (game)
        mov = input(f"({game.count:#03}) Entrez un mouvement (ex: AB) > ")
        mov = mov.strip()
        if not mov: return
        try:
            game.move(mov[0], mov[-1])
        except Exception as e:
            print(e)
        else:
            if len(game.stacks['B']) > size or len(game.stacks['C']) > size:
                print(game)
                print("🎈 Gagné !🎈")
                return

def solver():
    print("♖♖ Solver de Hanoi ♖♖")
    size = input("Taille de tour> ")
    game = Hanoi(int(size))
    print(game)
    game.solve('A', 'C')
    print(game)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Hanoi')
    parser.add_argument('-s', '--solver', action='store_true')
    args = parser.parse_args()
    if args.solver:
        solver()
    else:
        play()