

#calss header
class _SO():
	def __init__(self,): 
		self.name = "SO"
		self.definitions = [u'very, extremely, or to such a degree: ', u'used before a noun or before "not" to emphasize what is being said: ', u'used at the end of a sentence to mean to a very great degree: ', u'used usually before the verbs "have", "be", or "do", and other auxiliary verbs to express the meaning "in the same way" or "in a similar way": ', u'used to avoid repeating a phrase mentioned earlier: ', u'used to say that a situation mentioned earlier is correct or true: ', u'used to say that a fact that has just been stated is certainly true: ', u'used instead of repeating an adjective that has already been mentioned: ', u'used, especially by children, to argue against a negative statement: ', u'to act in the way mentioned: ', u'in this way, or like this: ', u'used when you are showing how something is done: ', u'used when you are representing the size of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
