

#calss header
class _DEFENCELESS():
	def __init__(self,): 
		self.name = "DEFENCELESS"
		self.definitions = [u'Defenceless people, animals, places, or things are weak and unable to protect themselves from attack: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
