

#calss header
class _OTHERWISE():
	def __init__(self,): 
		self.name = "OTHERWISE"
		self.definitions = [u'used to show that something is completely different from what you think it is or from what was previously stated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
