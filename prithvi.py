string = "Dream big";  
#Stores the reverse of given string  
reversedStr = "";  
   
#Iterate through the string from last and add each character to variable reversedStr  
for i in range(len(string)-1, -1, -1):  
    reversedStr = reversedStr + string[i];  
      
print("Original string: " + string);  
#Displays the reverse of given string  
print("Reverse of given string: " + reversedStr);  