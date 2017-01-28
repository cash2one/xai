

#calss header
class _FAHRENHEIT():
	def __init__(self,): 
		self.name = "FAHRENHEIT"
		self.definitions = [u'(of) a measurement of temperature on a standard in which 32\xb0 is the temperature at which water freezes and 212\xb0 that at which it boils: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
