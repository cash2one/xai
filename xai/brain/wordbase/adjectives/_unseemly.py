

#calss header
class _UNSEEMLY():
	def __init__(self,): 
		self.name = "UNSEEMLY"
		self.definitions = [u'not seemly (= socially suitable and polite)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
