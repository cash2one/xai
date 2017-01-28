

#calss header
class _RITZY():
	def __init__(self,): 
		self.name = "RITZY"
		self.definitions = [u'expensive and fashionable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
