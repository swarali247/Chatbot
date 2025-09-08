
#Greets user
print("Hello! I'm CyHelp.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

""" #Recounts start of Cybersecurity
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since your data breach !") """

print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")
input("Press enter to continue\n")

#Fun Fact
print("Did you know that the first computer virus ever discovered was in the year 1971 and was called The Creeper!")
input("Press enter to continue\n")

#Describes Cybersecurity
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from digital threats.")
print("These people can be governement, nations, individuals, companies, community organizations, and hackers.\n")

#Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, and availability")
print("Would you like to learn about the CIA Triad?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains pillars of CIA Triad
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) confidentiality, (b) integrity, (c) availability, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("Confidentiality makes sure data is private.")
  
  elif topic.lower() == "b":
    print("Integrity makes sure data has not been tampered with and can be trusted.")
  
  elif topic.lower() == "c":
    print("Availability makes sure authorized people can access the data.")
  
  elif topic.lower() == "d":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

print("Would you like to to take a short quiz to test your knowledge?")
quiz = input("Type 'yes' or 'no'\n")
if quiz.lower() == "yes":
  print("What does the C in CIA Triad stand for? \n")
  print("a) Confidence")
  print("b) Confidentiality")
  print("c) Creativity")
  print("d) None of the above")
  answer1 = input()
  if answer1.lower() == "b":
    print("Your answer was correct!")
  else:
    print("Unfortunatley, your answer was incorrect. The correct asnwer was b) Confidentiality")
  

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")