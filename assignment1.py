class Pupil:
    def __init__(self,roll,name,english,maths,physics,chemistry,CS):
        self.roll = roll
        self.name = name
        self.english = english
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
        self.CS = CS
    def show(self):
        print(f"name: {self.name}")
        print(f"english: {self.english}")
        print(f"maths: {self.maths}")
        print(f"physics: {self.physics}")
        print(f"chemistry: {self.chemistry}")
        print(f"CS: {self.CS}")
pupils = []
def main():
    print("Menu\n1.Report\n2.Admin\n3.Exit")
    while True:
        try:
            user_choice = int(input("enter your choice: "))
            if user_choice in [1,2,3]:
                break
            else:
                print("enter again")
                continue
        except:
            print("error,please choose again")
            user_choice = input("enter again")
    if user_choice == 1:
        print("admin menu\n1.creat people record\n2.display all pupils record\n4.modify pupils record\n5.delete peple record\n6.back to main menu")
        while True:
            try:
                choice = int(input("enter choice: "))
                if choice in [1,2,3,4,5,6]:
                    break
                else:
                    print("enter again")
                    continue
            except:
                print("enter again")
                choice = input("enter choice: ")
        if choice == 2:
            roll = int(input("enter roll number: "))
            name = input("enter name: ")
            english = input("enter mark in english: ")
            maths = input("enter mark in maths: ")
            physics = input("enter mark in physics: ")
            chemistry = input("enter mark in chemsitry: ")
            CS = input("enter mark in CS: ")
            pupil = Pupil(roll,name,english,maths,physics,chemistry,CS)
            pupils.append(pupil)
            while True:
                try:
                    next_choice = input("want to enter more record(y/n): ")
                    if next_choice == "n":
                        break
                    elif next_choice == "y":
                        continue
                    else:
                        int(a)
                except:
                    print("error")
                    next_choice = input("enter again")
        elif choice == 2:
            for i in pupils:
                i.show()
        elif choice == 3:
            for i in pupils:
                if i.roll == roll:
                    i.show()
        elif choice == 4:
            roll_pupil = input("enter roll: ")
            for i in pupils:
                if i.roll == roll_pupil:
                    name = input("enter name: ")
                    english = input("enter mark in english: ")
                    maths = input("enter mark in maths: ")
                    physics = input("enter mark in physics: ")
                    chemistry = input("enter mark in chemsitry: ")
                    CS = input("enter mark in CS: ")
                pupils[i] = Pupil(roll,name,english,maths,physics,chemistry,CS)
        else:
            roll_pupil = input("enter roll: ")
            for i in pupils:
                if i.roll == roll_pupil:
                    pupils.remove(i)
    elif user_choice == 1:
        while True:
            print("report menu\n1.class result\n2.pupil report class\n3.exit")
            choice = int(input("enter choice: "))
            if choice == 1:
                for i in pupils:
                    i.show()
            elif choice == 2:
                for i in pupils:
                    if i.roll == roll:
                        i.show()
    else:
        print("exit")
            
if __name__ == "__main__":
    main()
                