

#calss header
class _GUTTED():
	def __init__(self,): 
		self.name = "GUTTED"
		self.definitions = [u'extremely disappointed and unhappy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
