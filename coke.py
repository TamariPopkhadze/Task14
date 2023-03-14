def main():
  sum = 0
  while True :
    x = int(input("insert coin: "))
    if x== 5 or x == 10 or x == 25:
        sum = sum + x
        if sum < 50:
            print("Amount due", 50 - sum)
        else:
            print("Change owed", sum - 50)
            break
    else:
        print("Amount due" , 50 - sum)        
main()