

#calss header
class _DESIROUS():
	def __init__(self,): 
		self.name = "DESIROUS"
		self.definitions = [u'wanting something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
