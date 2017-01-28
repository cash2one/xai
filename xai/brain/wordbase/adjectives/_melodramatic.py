

#calss header
class _MELODRAMATIC():
	def __init__(self,): 
		self.name = "MELODRAMATIC"
		self.definitions = [u'showing much stronger emotions than are necessary or usual for a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
