

#calss header
class _ALOFT():
	def __init__(self,): 
		self.name = "ALOFT"
		self.definitions = [u'in the air or in a higher position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
