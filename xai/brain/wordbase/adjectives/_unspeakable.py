

#calss header
class _UNSPEAKABLE():
	def __init__(self,): 
		self.name = "UNSPEAKABLE"
		self.definitions = [u'too bad or shocking to be expressed in words: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
