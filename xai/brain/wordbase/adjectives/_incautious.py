

#calss header
class _INCAUTIOUS():
	def __init__(self,): 
		self.name = "INCAUTIOUS"
		self.definitions = [u'not showing or giving careful thought to the possible results: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
