

#calss header
class _DROWSY():
	def __init__(self,): 
		self.name = "DROWSY"
		self.definitions = [u'being in a state between sleeping and being awake: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
