n=137485
r=n%10
let_max=r
while n>0:
    r=n%10
    if(r<let_max):
        let_max=r
    n//=10
print(let_max)
