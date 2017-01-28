

#calss header
class _DECIDED():
	def __init__(self,): 
		self.name = "DECIDED"
		self.definitions = [u'certain, obvious, or easy to notice: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
