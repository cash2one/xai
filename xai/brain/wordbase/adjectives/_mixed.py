

#calss header
class _MIXED():
	def __init__(self,): 
		self.name = "MIXED"
		self.definitions = [u'showing a mixture of different feelings or opinions: ', u'including many different types of people or things: ', u'including both sexes: ', u'including people of different religions or races: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
