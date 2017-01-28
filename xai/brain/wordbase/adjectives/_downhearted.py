

#calss header
class _DOWNHEARTED():
	def __init__(self,): 
		self.name = "DOWNHEARTED"
		self.definitions = [u'unhappy and having no hope, especially because of a disappointment or failure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
