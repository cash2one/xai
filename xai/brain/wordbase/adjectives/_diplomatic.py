

#calss header
class _DIPLOMATIC():
	def __init__(self,): 
		self.name = "DIPLOMATIC"
		self.definitions = [u'involving diplomats or the management of the relationships between countries: ', u'acting in a way that does not cause offence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
