

#calss header
class _DAMAGING():
	def __init__(self,): 
		self.name = "DAMAGING"
		self.definitions = [u'causing harm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
