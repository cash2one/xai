

#calss header
class _PUNCHY():
	def __init__(self,): 
		self.name = "PUNCHY"
		self.definitions = [u'expressing something effectively and with power: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
