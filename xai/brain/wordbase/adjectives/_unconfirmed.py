

#calss header
class _UNCONFIRMED():
	def __init__(self,): 
		self.name = "UNCONFIRMED"
		self.definitions = [u'If facts are unconfirmed, it is not certain if they are true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
