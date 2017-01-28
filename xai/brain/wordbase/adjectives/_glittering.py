

#calss header
class _GLITTERING():
	def __init__(self,): 
		self.name = "GLITTERING"
		self.definitions = [u'exciting or admired by many people, usually relating to rich and famous people: ', u'shining with a lot of small bright flashes of light: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
