

#calss header
class _SWORN():
	def __init__(self,): 
		self.name = "SWORN"
		self.definitions = [u'formally and officially stated as being true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
