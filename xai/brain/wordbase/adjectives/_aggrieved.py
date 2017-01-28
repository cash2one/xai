

#calss header
class _AGGRIEVED():
	def __init__(self,): 
		self.name = "AGGRIEVED"
		self.definitions = [u'unhappy and angry because of unfair treatment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
