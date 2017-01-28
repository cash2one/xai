

#calss header
class _CONCOMITANT():
	def __init__(self,): 
		self.name = "CONCOMITANT"
		self.definitions = [u'happening and connected with another thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
