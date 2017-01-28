

#calss header
class _DISTRAUGHT():
	def __init__(self,): 
		self.name = "DISTRAUGHT"
		self.definitions = [u'extremely worried, nervous, or upset: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
