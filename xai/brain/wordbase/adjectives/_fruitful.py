

#calss header
class _FRUITFUL():
	def __init__(self,): 
		self.name = "FRUITFUL"
		self.definitions = [u'producing good results: ', u'If a person is fruitful, they produce a lot of children.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
