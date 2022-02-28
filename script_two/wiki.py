import wikipedia

#engine = 'WolframAlpha'


def printDefinition():
    ans = wikipedia.summary('dpdgroup')
    return ans
def printGivenDefinition(query):
    return wikipedia.summary(query, 1)


print(printDefinition())
# print(printGivenDefinition(engine))
