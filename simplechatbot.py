class chatbot:
    def __init__(self):
        self.username=" " # it means it intially empty in the first
        self.password=" " # same password also initially empty
        self.loggdin=False
        self.menu()

    def menu(self):
        user_input=input('''                    ----Welcome User in my chatbot----
                       ----How do u wanna proceed----
                    1.Press 1 for Signup
                    2.Press 2 for SignIn
                    3.Press 3 for Write post
                    4.Press 4 for Post your Post
                    5.Press any key if you want to exit
                    -->  ''') # form here u simply take the user input
        if user_input=="1":
            self.Signup()
        if user_input=="2":
            self.Signin()
        if user_input=="3":
            self.Mypost()
        if user_input=="4":
            self.Post()
        if user_input==" ":
            exit()

    def Signup(self):
        user=input("User please enter your username : ") 
        password=input("User please enter your password : ")

        self.username=user
        self.password=password
        print("----User you are successfully sigup----")
        print("\n")
        print("\n")
        self.menu()
    
    def Signin(self):
        if self.username==" " and self.password==" ": # here u check if user not filed username and password then message show that u need to signin first 
            print("User you need to Signup first")
        else:
            user=input("User enter your username: ")
            password=input("User enter your passwrod: ")
            if self.username==user and self.password==password:
                print("----User your are successfully login----")
                self.loggdin=True
                print("\n")
                print("\n")
                self.menu()
            else:
                print("----User your UserID and password is Invalid----")
                exit()

    def Mypost(self):
        if self.loggdin==True:
            user1=input("User write the your  message-->")
            print(f"User your message is-->{user1}")
            print("---Your message is ready to post---")
        else:
            print("!!!!!User you need to Press 1!!!!!")
        self.menu()

    def Post(self):
        if self.loggdin==True:
            friend=input("Type your friend name that u want to send the message: ")
            print(f"Conngratulation user your  message is successfully Post to {friend}")
        else:
            print("!!!!!User you  need to press 1!!!!!!")
        self.menu()

    


user1=chatbot()

