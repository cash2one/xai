

#calss header
class _UPRIGHT():
	def __init__(self,): 
		self.name = "UPRIGHT"
		self.definitions = [u'straight up or vertical: ', u'used to refer to something that is taller than it is wide: ', u'honest, responsible, and moral: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
