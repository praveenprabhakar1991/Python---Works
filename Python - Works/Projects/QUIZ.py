# WAP for QUIZ Game

print("\n Welcome to KBC \n")

questions = [
            ['1)  Which software controls the hardware of the computer ?', 'Application', 'System', 'Program', 'Memory', 'b'],
            ['2)  What are portable computers for traveling users ?', 'Super Computer', 'USB', 'Laptop', 'Mini Computer', 'c'],
            ['3)  What is the meaning of KB attached to the computer ?', 'Kit Bit', 'Kilobyte', 'Key Block', 'Kernel Boot', 'b'],
            ['4)  By computer process ......... are converted into information.', 'Data', 'Number', 'Processor', 'Input', 'a'],
            ['5)  What is the full form of OSI in a network?', 'Open Source Interconnection', 'Open Software Interconnection', 'Old Source Interconnection', 'Open Systems Interconnection', 'd'],
            ['6)  Which of the following is not an internet protocol ?', 'UDP', 'TCP/IP', 'ASCII', 'FTP / ip', 'c'],
            ['7)  What is the name of the file which is attached to the email and sent to the recipient of the email ?', 'Attachment', 'Annexure', 'Appendage', 'Add-on', 'a'],
            ['8)  Which of the following drives computer hardware and acts as a platform for running other software ?', 'Application software', 'Operating System', 'supercomputer', 'RAM', 'b'],
            ['9)  Which is the fastest computer ?', 'Mainframe', 'Microcomputer', 'Workstation', 'supercomputer', 'd'],
            ['10) How many digits are included in the Aadhar card number ?', '8', '12', '10', '16', 'b'],
            ['11) Which of the following is not application software ?', 'Windows XP', 'VLC Media Player', 'Adobe Reader', 'Photoshop', 'a'],
            ['12) What is the full form of OTP ?', 'One the phone', 'One Time Password', 'Out to practice', 'One Time Programmable', 'b'],
            ['13) Which of the following is an example of an e-commerce website ?', 'Twitter', 'Facebook', 'Flipkart', 'Instagram', 'c'],
            ['14) Which of the following is not an example of a mobile wallet ?', 'G-Pay', 'Bhim', 'Credit card', 'Pay-TM', 'c'],
            ['15) Which of the following authority has issued Aadhar card ?', 'AAI', 'UIDAI', 'NHAI', 'UIDIA', 'b'],
            ]

prize = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]

    print(f'The Question for {prize[i]} is : \n')
    print(f'{question[0]}\n')
    print(f'    A. {question[1]}               B. {question[2]}')
    print(f'    C. {question[3]}               D. {question[4]}\n')

    answer = input('Choose your Answer (A-D) or Q to Quit : ').lower()

    if answer == 'q':
        money = prize[i-1]        
        break   
    
    if answer == question[-1]:
        print(f'Correct Answer, You have Won Rs.{prize[i]}\n')

        if i < 4:
            money = 0
            
        elif i >= 4 and i < 9:
            money = 10000
            print('Congrats, You have Rs.10000 with You')
        elif i >= 9 and i < 14:
            money = 320000
            print('Congrats, You have Rs.320000 with You')
        elif i >= 14:
            money = 10000000                
    else:
        print('Wrong Answer.')       
        break  
    
print(f'Your take home prize is Rs.{money}\n')  