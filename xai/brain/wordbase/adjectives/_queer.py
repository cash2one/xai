

#calss header
class _QUEER():
	def __init__(self,): 
		self.name = "QUEER"
		self.definitions = [u'(especially of a man) gay', u'strange, unusual, or not expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
