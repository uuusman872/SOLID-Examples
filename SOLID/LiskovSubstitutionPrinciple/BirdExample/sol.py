

class Bird:
    def __init__(self, name):
        self.name = name
        self.feathers = 2
        self.beack = True
    def fly_or_run(self):
        pass


class FlyingBirds(Bird):
    def fly_or_run(self):
        print(f"[+] I am flying biach")


class RunningBirds(Bird):
    def fly_or_run(self):
        print(f"[+] Eat my mother footing dust")


class Chicken(RunningBirds):
    pass


class Pigon(FlyingBirds):
    pass



def main(bird: Bird):
    bird.fly_or_run()



if __name__ == "__main__":
    main(bird=Chicken("chicky"))