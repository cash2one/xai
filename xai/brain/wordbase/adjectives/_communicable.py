

#calss header
class _COMMUNICABLE():
	def __init__(self,): 
		self.name = "COMMUNICABLE"
		self.definitions = [u'able to be given from one person to another: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
