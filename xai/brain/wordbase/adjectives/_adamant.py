

#calss header
class _ADAMANT():
	def __init__(self,): 
		self.name = "ADAMANT"
		self.definitions = [u'impossible to persuade, or unwilling to change an opinion or decision: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
