

#calss header
class _DESERVEDLY():
	def __init__(self,): 
		self.name = "DESERVEDLY"
		self.definitions = [u'If something happens to you deservedly, you deserve it to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
