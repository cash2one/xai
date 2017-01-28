

#calss header
class _REVERENT():
	def __init__(self,): 
		self.name = "REVERENT"
		self.definitions = [u'showing great respect and admiration: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
