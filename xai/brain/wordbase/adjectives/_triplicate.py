

#calss header
class _TRIPLICATE():
	def __init__(self,): 
		self.name = "TRIPLICATE"
		self.definitions = [u'existing in three parts that are exactly the same']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
