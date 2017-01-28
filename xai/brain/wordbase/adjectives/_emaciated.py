

#calss header
class _EMACIATED():
	def __init__(self,): 
		self.name = "EMACIATED"
		self.definitions = [u'very thin and weak, usually because of illness or extreme hunger: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
