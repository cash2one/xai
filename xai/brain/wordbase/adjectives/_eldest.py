

#calss header
class _ELDEST():
	def __init__(self,): 
		self.name = "ELDEST"
		self.definitions = [u'being the oldest of three or more people, especially within a family: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
