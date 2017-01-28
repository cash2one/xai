

#calss header
class _DREAMLESS():
	def __init__(self,): 
		self.name = "DREAMLESS"
		self.definitions = [u'Dreamless sleep is sleep in which you do not dream: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
