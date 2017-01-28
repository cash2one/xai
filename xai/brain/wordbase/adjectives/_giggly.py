

#calss header
class _GIGGLY():
	def __init__(self,): 
		self.name = "GIGGLY"
		self.definitions = [u'giggling a lot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
