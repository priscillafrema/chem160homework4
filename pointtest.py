from point import address
p1=point(3,(1., 2., 3.))
p2=point(3,(6., 7., 8.))
x = p1.dist(p2)
print(x)
p2.mirror()
    def __init__(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i]))
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i)+" "
        return output
    def scale(self, x):
        for i in range(self.dim):
            self.data[i]*=x
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i]*apoint.data[i]
        return sum

    def dist(self,p2):
        return math.sqrt((self.data[0]-p2.data[0]**2 +(self.data[1]-p2.data[1]**2+(self.data[2]-p2.data[2])**2)

    def mirror(self):
        for i in range (0, len(self.data)):
            self.data[i] = -self.data[i]
        print(self.data)
