

#calss header
class _LEEWARD():
	def __init__(self,): 
		self.name = "LEEWARD"
		self.definitions = [u'(on the side of a ship, etc.) facing away from the wind']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
