

#calss header
class _INIMICAL():
	def __init__(self,): 
		self.name = "INIMICAL"
		self.definitions = [u'harmful or limiting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
