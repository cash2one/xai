

#calss header
class _PARANORMAL():
	def __init__(self,): 
		self.name = "PARANORMAL"
		self.definitions = [u'impossible to explain by known natural forces or by science: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
