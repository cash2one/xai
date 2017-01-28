

#calss header
class _MIDDLEBROW():
	def __init__(self,): 
		self.name = "MIDDLEBROW"
		self.definitions = [u'Middlebrow music, literature, art, and films are of good quality, interesting, and often popular, but can be understood quite easily.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
