

#calss header
class _THICKSET():
	def __init__(self,): 
		self.name = "THICKSET"
		self.definitions = [u'A thickset person, especially a man, has a body that is wide across the shoulders and chest and is short: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
