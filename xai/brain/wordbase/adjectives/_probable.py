

#calss header
class _PROBABLE():
	def __init__(self,): 
		self.name = "PROBABLE"
		self.definitions = [u'likely to be true or likely to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
