

#calss header
class _PHOBIC():
	def __init__(self,): 
		self.name = "PHOBIC"
		self.definitions = [u'having a strong dislike of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
