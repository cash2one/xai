

#calss header
class _IMPECCABLE():
	def __init__(self,): 
		self.name = "IMPECCABLE"
		self.definitions = [u'perfect, with no problems or bad parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
