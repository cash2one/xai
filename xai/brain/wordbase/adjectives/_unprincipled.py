

#calss header
class _UNPRINCIPLED():
	def __init__(self,): 
		self.name = "UNPRINCIPLED"
		self.definitions = [u'having or showing no moral rules or standards of good behaviour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
