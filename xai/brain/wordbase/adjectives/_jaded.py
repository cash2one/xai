

#calss header
class _JADED():
	def __init__(self,): 
		self.name = "JADED"
		self.definitions = [u'not having interest or losing interest because you have experienced something too many times: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
