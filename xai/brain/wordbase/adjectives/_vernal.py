

#calss header
class _VERNAL():
	def __init__(self,): 
		self.name = "VERNAL"
		self.definitions = [u'relating to or happening in the spring']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
