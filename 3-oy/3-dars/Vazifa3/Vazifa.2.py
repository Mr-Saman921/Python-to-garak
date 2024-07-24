class Hero:
    def __init__(self, name: str, life: int, rank: float):
        if not isinstance(name, str):
            raise TypeError(f"Expected 'name' to be a string, got {type(name).__name__}")
        if not isinstance(life, int):
            raise TypeError(f"Expected 'life' to be an integer, got {type(life).__name__}")
        if not isinstance(rank, float):
            raise TypeError(f"Expected 'rank' to be a float, got {type(rank).__name__}")

        self.name = name
        self.life = life
        self.rank = rank

if __name__ == "__main__":
    try:
        hero1 = Hero("Superman", 100, 9.5)
        print(f"Hero '{hero1.name}' created with life: {hero1.life} and rank: {hero1.rank}")

    except TypeError as e:
        print(f"Error creating hero: {e}")
