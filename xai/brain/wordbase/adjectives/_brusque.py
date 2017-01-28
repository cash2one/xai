

#calss header
class _BRUSQUE():
	def __init__(self,): 
		self.name = "BRUSQUE"
		self.definitions = [u'quick and rude in manner or speech: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
