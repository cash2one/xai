

#calss header
class _ODIOUS():
	def __init__(self,): 
		self.name = "ODIOUS"
		self.definitions = [u'extremely unpleasant and causing or deserving hate: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
