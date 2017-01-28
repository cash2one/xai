

#calss header
class _PARTICULAR():
	def __init__(self,): 
		self.name = "PARTICULAR"
		self.definitions = [u'special, or this and not any other: ', u'especially: ', u'not easily satisfied and demanding that close attention should be given to every detail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
