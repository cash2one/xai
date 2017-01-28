

#calss header
class _SHIPBOARD():
	def __init__(self,): 
		self.name = "SHIPBOARD"
		self.definitions = [u'happening or used on a ship: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
