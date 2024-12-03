def S(file_name):
    try:
        with open(file_name,"r")as file:
         sum=0
         for line in file:
            if line.strip().isdigit():
               sum+=int(line.strip())
        return sum
    
    except FileNotFoundError:
       print(" File not found")
       return None

file_name="numbers.txt"

result= S(file_name)
if result is not None:
   print(" The sum is",result)


 