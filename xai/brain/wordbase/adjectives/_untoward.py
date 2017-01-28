

#calss header
class _UNTOWARD():
	def __init__(self,): 
		self.name = "UNTOWARD"
		self.definitions = [u'unexpected and not convenient or unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
