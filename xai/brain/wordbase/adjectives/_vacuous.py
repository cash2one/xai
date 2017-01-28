

#calss header
class _VACUOUS():
	def __init__(self,): 
		self.name = "VACUOUS"
		self.definitions = [u'not expressing or showing intelligent thought or purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
