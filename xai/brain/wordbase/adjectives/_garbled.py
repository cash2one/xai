

#calss header
class _GARBLED():
	def __init__(self,): 
		self.name = "GARBLED"
		self.definitions = [u'If words or messages are garbled, they are not clear and are very difficult to understand, often giving a false idea of the facts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
