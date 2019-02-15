class Sol:
    def remove_duplicates(self,list):
        next_new=0
        for i in range(len(list)):
            if list[i]!=list[i-1]:
                next_new+=1
        return next_new

if __name__ == '__main__':
    list=[1,1,5]
    p1=Sol()
    print(p1.remove_duplicates(list))
