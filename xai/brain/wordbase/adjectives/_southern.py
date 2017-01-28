

#calss header
class _SOUTHERN():
	def __init__(self,): 
		self.name = "SOUTHERN"
		self.definitions = [u'in or from the south part of an area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
