

#calss header
class _REPRODUCIBLE():
	def __init__(self,): 
		self.name = "REPRODUCIBLE"
		self.definitions = [u'able to be shown, done, or made again: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
