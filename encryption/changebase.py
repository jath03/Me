
def changebase_from_10(number, wanted_base):
   if number != int(number):
      raise ValueError('Number not whole')
   elif wanted_base < 2:
      raise ValueError('Too small')
   elif wanted_base != int(wanted_base):
      raise ValueError('Base not whole')
   else:
      Ndigits=1
      final_answer=''
      while number >= wanted_base**Ndigits:
         Ndigits=Ndigits+1
      digits=[]
      newnumber=number
      for digitcounter in range(1, Ndigits+1):
         placevalue=wanted_base**(Ndigits-digitcounter)
         digitvalue=int(newnumber/placevalue)
         digits.append(str(digitvalue))
         final_answer=final_answer+str(digitvalue)
         newnumber=newnumber-digitvalue*placevalue
      return final_answer

def changebase_to_10(number, current_base):
   if number != int(number):
      raise ValueError('Number not whole')
   elif current_base < 2:
      raise ValueError('Too small')
   elif current_base != int(current_base):
      raise ValueError('Base not whole')
   else:
      Ndigits=1
      while number >= 10**Ndigits:
         Ndigits=Ndigits+1
      answer=0
      while Ndigits > 0:
         divisor=10**(Ndigits-1)
         nextdigit=int(number/divisor)
         if nextdigit >= current_base:
            print('invalid number')
            return
         else:
            answer=answer+nextdigit*current_base**(Ndigits-1)
            number=number-nextdigit*10**(Ndigits-1)
            Ndigits=Ndigits-1
      return answer

def changebase(number, current_base, wanted_base):
    answer1=changebase_to_10(number, current_base)
    final_answer=changebase_from_10(answer1, wanted_base)
    return final_answer
    
    
