

#calss header
class _SUCCESSFUL():
	def __init__(self,): 
		self.name = "SUCCESSFUL"
		self.definitions = [u'achieving the results wanted or hoped for: ', u'having achieved a lot, become popular, and/or made a lot of money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
