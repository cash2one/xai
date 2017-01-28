

#calss header
class _DELINQUENT():
	def __init__(self,): 
		self.name = "DELINQUENT"
		self.definitions = [u'illegal or not acceptable, or behaving in a way that is illegal or not acceptable: ', u'late (in paying money owed): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
