class Car :
    # creating a constructor
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    def drive(self):
        print("Drive the car")
    def stop(self):
        print("Stop the car")
        