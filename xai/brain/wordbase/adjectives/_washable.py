

#calss header
class _WASHABLE():
	def __init__(self,): 
		self.name = "WASHABLE"
		self.definitions = [u'able to be washed in a washing machine without being damaged: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
