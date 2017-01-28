

#calss header
class _OFFBEAT():
	def __init__(self,): 
		self.name = "OFFBEAT"
		self.definitions = [u'unusual and strange and therefore surprising or noticeable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
