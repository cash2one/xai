

#calss header
class _FALSE():
	def __init__(self,): 
		self.name = "FALSE"
		self.definitions = [u'not real, but made to look or seem real: ', u'not true, but made to seem true in order to deceive people: ', u'If you do something under false pretences, you lie about who you are, what you are doing, or what you intend to do, in order to get something: ', u'not correct: ', u'not sincere or expressing real emotions: ', u'A false friend is not loyal or cannot be trusted.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
