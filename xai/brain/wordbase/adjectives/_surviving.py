

#calss header
class _SURVIVING():
	def __init__(self,): 
		self.name = "SURVIVING"
		self.definitions = [u'continuing to live or exist: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
