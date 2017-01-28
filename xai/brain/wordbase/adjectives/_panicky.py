

#calss header
class _PANICKY():
	def __init__(self,): 
		self.name = "PANICKY"
		self.definitions = [u'feeling suddenly very worried or frightened: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
