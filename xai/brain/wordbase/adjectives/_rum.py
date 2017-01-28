

#calss header
class _RUM():
	def __init__(self,): 
		self.name = "RUM"
		self.definitions = [u'unusual and strange: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
