

#calss header
class _UNLEADED():
	def __init__(self,): 
		self.name = "UNLEADED"
		self.definitions = [u'Unleaded petrol or other substance does not contain lead: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
