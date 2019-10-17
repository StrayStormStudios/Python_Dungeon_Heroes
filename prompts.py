#gets user input and returns a response
def prompt_usr(prompt, typ):
    if typ == "number":
        response = input(prompt)
        while not response.isnumeric():
            print("Try again: ")
            response = input(prompt)
        #print("Entering response {}".format(response))
        return int(response)
    elif typ == "string":
        response = input(prompt)
        while not response.isalpha():
            print("try again: ")
            response = input(prompt)
        #print("Entering response {}".format(response))
        return str(response)
