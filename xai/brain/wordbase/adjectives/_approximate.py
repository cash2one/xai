

#calss header
class _APPROXIMATE():
	def __init__(self,): 
		self.name = "APPROXIMATE"
		self.definitions = [u'not completely accurate but close: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
