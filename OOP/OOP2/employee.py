class employee:
        def staff(self,name,salary):
            self.name = name
            self.saraly = salary
            print("Employee's name is {} and salary is {}".format(name,salary))


em = employee()
print(em.staff("Paul",100))
