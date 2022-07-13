#using slice 
my_list = [1,2,3,4,5,6]

new_list = my_list[2:5]

print(new_list)






#slice

my_list = [1,2,3,4,5,6]

print(my_list[1:4:2])

#start_position:  end_position   :   start_position - end_position







#file handeling 

from email import message


f1 = open('message.txt','r')

# message = 'hi my name is salman and currently learnig python'
message1 = f1.read(6)
print(message1)
f1.close()
f1 = open('message.txt','r')
message2 = f1.read()
print(message2)









#using append and read 

from email import message


f1 = open('message.txt','a')
text = 'this is the next line\n'
f1.write(text)
f1.close()

f1 = open('message.txt','r')
text = f1.read()
print(text)
f1.close()
