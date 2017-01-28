

#calss header
class _OAKEN():
	def __init__(self,): 
		self.name = "OAKEN"
		self.definitions = [u'made of oak wood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
