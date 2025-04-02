class Robot:
    """Represents a robot, with a name."""
    population = 0
    
    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print(f'{self.name} 로봇이 생성되었습니다.')
        Robot.population += 1
        
    def die(self):
        """I'm dying."""
        print(f'{self.name} 로봇이 소멸되었습니다.')
        Robot.population -= 1
        if Robot.population == 0:
            print(f'{self.name} 로봇이 마지막입니다.')
        else:
            print(f'현재 남아있는 로봇은 {Robot.population}대입니다.')
        
    def say_hi(self):
        """Greeting by the robot.
        Yeah, they can do that."""
        print(f'안녕하세요, 제 이름은 {self.name}입니다.')

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print(f'현재 남아있는 로봇은 {cls.population}대입니다.')
        
droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\n로봇들이 이곳에서 일을 할 수 있습니다.")
print("로봇들이 일을 끝냈으면 파괴하겠습니다.")

droid1.die()
droid2.die()

Robot.how_many()
