

#calss header
class _RECESSED():
	def __init__(self,): 
		self.name = "RECESSED"
		self.definitions = [u'built in a space in a wall: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
