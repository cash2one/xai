

#calss header
class _FATEFUL():
	def __init__(self,): 
		self.name = "FATEFUL"
		self.definitions = [u'having an important and usually negative effect on the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
