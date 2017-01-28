

#calss header
class _OPTIMISTIC():
	def __init__(self,): 
		self.name = "OPTIMISTIC"
		self.definitions = [u'hoping or believing that good things will happen in the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
