

#calss header
class _MINI():
	def __init__(self,): 
		self.name = "MINI"
		self.definitions = [u'very short and covering only the very top part of the leg: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
