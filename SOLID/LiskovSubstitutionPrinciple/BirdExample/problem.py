



class Bird:
    def fly():
        print(f"[+] Flying in the sky")


class Pigon(Bird):
    def fly(self):
        print(f"[+] Pigon is flying ")


class Chicken(Bird):
    def fly(self): # Violates LSP because chicken is not replaceable with Bird class 
        raise NotImplementedError("hah Chickens do not fly :) ")


def main(bird: Bird):
    bird.fly()

if __name__ == "__main__":
    main(bird=Chicken())















