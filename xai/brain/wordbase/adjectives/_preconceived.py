

#calss header
class _PRECONCEIVED():
	def __init__(self,): 
		self.name = "PRECONCEIVED"
		self.definitions = [u'(of an idea or an opinion) formed too early, especially without enough thought or knowledge: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
