

#calss header
class _POLITE():
	def __init__(self,): 
		self.name = "POLITE"
		self.definitions = [u"behaving in a way that is socially correct and shows understanding of and care for other people's feelings: ", u'socially correct rather than friendly: ', u'people who have been taught how to behave in a socially correct way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
