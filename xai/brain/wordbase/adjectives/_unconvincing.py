

#calss header
class _UNCONVINCING():
	def __init__(self,): 
		self.name = "UNCONVINCING"
		self.definitions = [u'If an explanation or story is unconvincing, it does not sound or seem true or real: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
