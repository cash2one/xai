

#calss header
class _DESICCATED():
	def __init__(self,): 
		self.name = "DESICCATED"
		self.definitions = [u'dried, with the moisture removed: ', u'not interesting or completely without imagination: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
