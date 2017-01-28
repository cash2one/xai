

#calss header
class _HYPOCRITICAL():
	def __init__(self,): 
		self.name = "HYPOCRITICAL"
		self.definitions = [u'saying that you have particular moral beliefs but behaving in a way that shows these are not sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
