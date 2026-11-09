
def limit(a,limitation):
          count=0
          for i in a:
              if i<limitation:
                  count+=1
          return count
a=[23,34,23,1123,10,23]          
print(limit(a,20))
  
