

#calss header
class _OVERCROWDED():
	def __init__(self,): 
		self.name = "OVERCROWDED"
		self.definitions = [u'containing too many people or things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
