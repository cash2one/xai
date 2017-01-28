

#calss header
class _PREPARATORY():
	def __init__(self,): 
		self.name = "PREPARATORY"
		self.definitions = [u'done in order to get ready for something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
