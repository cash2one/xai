

#calss header
class _METRIC():
	def __init__(self,): 
		self.name = "METRIC"
		self.definitions = [u'using or relating to a system of measurement that uses metres, centimetres, litres, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
