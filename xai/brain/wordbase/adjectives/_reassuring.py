

#calss header
class _REASSURING():
	def __init__(self,): 
		self.name = "REASSURING"
		self.definitions = [u'making you feel less worried: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
