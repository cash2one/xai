

#calss header
class _PRAY():
	def __init__(self,): 
		self.name = "PRAY"
		self.definitions = [u'a forceful way of saying "please": ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
