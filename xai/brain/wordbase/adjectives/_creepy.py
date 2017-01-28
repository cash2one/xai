

#calss header
class _CREEPY():
	def __init__(self,): 
		self.name = "CREEPY"
		self.definitions = [u'strange or unnatural and making you feel frightened: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
