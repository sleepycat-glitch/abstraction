# learning abstraction
# abstraction means to simplify complex code or wrap complex code into a box called a function

def speech(): 
    dream_speech = "And when this happens, and when we allow freedom ring, when we let it ring from every village and every hamlet, from every state and every city, we will be able to speed up that day when all of God's children, Black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual: Free at last. Free at last. Thank God almighty, we are free at last."

    word = "freedom"

    if word in dream_speech:
        print("Freedom found.")
    else: 
        print("Not found.")

    question = input("Did you find the word?")
    print("Your response is :", question)

# calling a function
speech()
speech()