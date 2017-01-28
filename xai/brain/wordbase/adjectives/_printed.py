

#calss header
class _PRINTED():
	def __init__(self,): 
		self.name = "PRINTED"
		self.definitions = [u'information in the form of books, newspapers, and magazines: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
