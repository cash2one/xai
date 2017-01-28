

#calss header
class _ABAFT():
	def __init__(self,): 
		self.name = "ABAFT"
		self.definitions = [u'at the back of or behind a ship or boat']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
