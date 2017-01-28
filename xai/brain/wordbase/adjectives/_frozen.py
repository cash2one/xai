

#calss header
class _FROZEN():
	def __init__(self,): 
		self.name = "FROZEN"
		self.definitions = [u'(of water) turned into ice, or (of food) preserved by freezing: ', u'If a person, or a part of their body is frozen, they are very cold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
