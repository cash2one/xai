

#calss header
class _INTERDENOMINATIONAL():
	def __init__(self,): 
		self.name = "INTERDENOMINATIONAL"
		self.definitions = [u'shared by different groups of the Christian Church: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
