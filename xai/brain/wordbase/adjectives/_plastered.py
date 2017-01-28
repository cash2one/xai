

#calss header
class _PLASTERED():
	def __init__(self,): 
		self.name = "PLASTERED"
		self.definitions = [u'extremely drunk: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
