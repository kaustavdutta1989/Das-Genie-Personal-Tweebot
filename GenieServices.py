import GenieActions

GenieActions.greetings()    # Called upon Genie Wake Up

# Always Ready to Serve
while True:
    # takeCommand()
    # not working... therefore not included into the final project.

    # Get User Input for Bot
    userInput = input('You: ')

    # Convolute to get Bot Response
    botResponse = GenieActions.getCommandResponse(userInput.lower())

    # Print the Response to the User
    GenieActions.speak(botResponse)
