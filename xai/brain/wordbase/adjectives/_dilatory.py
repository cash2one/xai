

#calss header
class _DILATORY():
	def __init__(self,): 
		self.name = "DILATORY"
		self.definitions = [u'slow and likely to cause delay: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
