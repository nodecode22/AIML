from datetime import datetime
class User:
    def __init__(self,username):
        self.username=username

    def __str__(self):
        return self.username


class Message:
    def __init__(self,sender,content):
        self.sender=sender
        self.content=content
        self.time=datetime.now().strftime("%H%M%S")

    def __str__(self):
        return f"[{self.time}] {self.sender}: {self.content}"
        

class Chatroom:
    def __init__(self,room_name):
        self.room_name=room_name
        self.users=[]
        self.messages=[]

    def join(self,user):
        if user not in self.users:
            self.users.append(user)
        print(f"{user} joined the chatroom.")
    def leave(self,user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user} left the chat room")
    def send_message(self,user,content):
        if user in self.users:
            message=Message(user,content)
            self.messages.append(message)
            print(message)
        else:
            print(f"{user} is not in the char room")
    def show_history(self):
        print(f"\n----------Chat History: {self.room_name}")

        if not self.messages:
            print("no message yet!!")
        else:
            for message in self.messages:
                print(message)

    def show_user(self):
        print("\n Users currently in room: ")
        for user in self.users:
            print("-",user)

#creating user

user1=User("Saurabh")
user2=User("David")
user3=User("Rohan")


# creating the chat room

room=Chatroom("Python Group")

#Users Joining

room.join(user1)
room.join(user2)
room.join(user3)


#show users in room

room.show_user()

#sending message
room.send_message(user1,"Hello everyone")
room.send_message(user2,"HI Saurabh")
room.send_message(user3,"Lets meet at college")
room.send_message(user1,"Ok Done!!")

#users leaving

room.leave(user3)

#chat history

room.show_history()

room.send_message(user3,"I am back")
