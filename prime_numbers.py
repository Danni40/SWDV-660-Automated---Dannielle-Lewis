def is_prime(x):

   for x in range(1, 101, 2):

       if x % 2 == 0 or x % 3 == 0:

           print(x , "Not Prime")

       else:

           if x % 2 != 0 or x % 3 != 0:

               print(x , "is a prime number")

             

print(is_prime(1))