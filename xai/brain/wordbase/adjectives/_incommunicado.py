

#calss header
class _INCOMMUNICADO():
	def __init__(self,): 
		self.name = "INCOMMUNICADO"
		self.definitions = [u'not communicating with anyone else because you do not want to or are not allowed to: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
