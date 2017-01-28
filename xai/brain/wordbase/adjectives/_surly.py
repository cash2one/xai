

#calss header
class _SURLY():
	def __init__(self,): 
		self.name = "SURLY"
		self.definitions = [u'often in a bad mood, unfriendly, and not polite: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
