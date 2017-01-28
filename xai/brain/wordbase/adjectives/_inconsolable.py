

#calss header
class _INCONSOLABLE():
	def __init__(self,): 
		self.name = "INCONSOLABLE"
		self.definitions = [u'so sad or disappointed that it is impossible for anyone to make you feel better: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
