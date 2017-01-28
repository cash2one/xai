

#calss header
class _ENVIABLE():
	def __init__(self,): 
		self.name = "ENVIABLE"
		self.definitions = [u'If someone is in an enviable situation, you wish you were also in that situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
