

#calss header
class _PREVENTIVE():
	def __init__(self,): 
		self.name = "PREVENTIVE"
		self.definitions = [u'intended to stop something before it happens: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
