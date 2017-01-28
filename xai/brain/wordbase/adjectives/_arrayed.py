

#calss header
class _ARRAYED():
	def __init__(self,): 
		self.name = "ARRAYED"
		self.definitions = [u'dressed in a particular way, especially in beautiful clothes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
