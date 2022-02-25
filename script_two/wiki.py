import wikipedia

def printDefinition():
    return wikipedia.summary('dpdgroup', 1)

print(printDefinition())
