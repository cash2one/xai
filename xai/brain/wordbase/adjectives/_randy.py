

#calss header
class _RANDY():
	def __init__(self,): 
		self.name = "RANDY"
		self.definitions = [u'feeling a lot of sexual desire']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
