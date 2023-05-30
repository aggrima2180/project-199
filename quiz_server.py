import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

clients  = []

questions = [
         "what is the Italian word for PIE?  \n a.Mozarella \n b.pasty \n c.patty \n d.pizza",
         "water boils at 212 units at which scale? \n a.fahrenhiet \n b.celsius \n c.rankine \n d.kelvin",
         "which sea creature hac three hearts? \n a.Dolphin \n b.Octopus \n c.Walrus \n d.seal",
         "who was the character famous in our childhood rymes associated with a lamb? \n a.Mary \n b.jack \n c.jhonny \n d.Mukesh",
         "who is loki? \n a.god of Thunder \n b.God of Dwarves \n c.god of mischief \n d.God of Gods",
         "what is the smallest continent? \n a.Asia \n b.Antartica \n c.Africa \n d.Australlia"
]

while True:
    conn,adder  = server.accept()
    list_of_clients.append(conn)
    print(addr[0]+ "connected")

    new_thread = Thread(targets = clientsthread, args =(conn,addr))
    new_thread.start()
       

def remove_question(index):
    questions.pop(index)
    answer.pop(index)

def clientthread(conn):
    score = 0
    conn,send("welcome to this quiz game!".emcode('utf-8'))
    conn.send("you will recieve a question the answer to that question")
    conn.send("GOOD LUCK!\n\n".encode('utf-8'))
    index,question,answer  = get_random_question_answer(conn)
    while True:
        try:
            message =  conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score+=1
                    conn.send(f"Bravo! your score is {score}\n\n".encode('utf-8'))
                else
                    conn.send(f"Incorrect answer! Better lick next time\n\n".encode('utf-8'))
                remove_question(index)
                index,question,answer = get_random_question_answer(conn)
            else:
                remove(conn)
        expect:
            continue
    
def get_random_question_answer(conn):
    random_index = random.radient(0,len(questions) - 1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer
