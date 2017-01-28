

#calss header
class _SHAKESPEAREAN():
	def __init__(self,): 
		self.name = "SHAKESPEAREAN"
		self.definitions = [u'written by William Shakespeare, or relating to or typical of his work : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
