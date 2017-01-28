

#calss header
class _PRECISE():
	def __init__(self,): 
		self.name = "PRECISE"
		self.definitions = [u'exact and accurate: ', u'very careful and accurate, especially about small details: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
