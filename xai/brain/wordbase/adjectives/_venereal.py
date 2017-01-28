

#calss header
class _VENEREAL():
	def __init__(self,): 
		self.name = "VENEREAL"
		self.definitions = [u'caused or spread by sexual activity with another person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
