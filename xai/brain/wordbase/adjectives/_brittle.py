

#calss header
class _BRITTLE():
	def __init__(self,): 
		self.name = "BRITTLE"
		self.definitions = [u'delicate and easily broken: ', u'unkind and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
