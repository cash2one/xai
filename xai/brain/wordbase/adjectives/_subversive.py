

#calss header
class _SUBVERSIVE():
	def __init__(self,): 
		self.name = "SUBVERSIVE"
		self.definitions = [u'trying to destroy or damage something, especially an established political system: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
