

#calss header
class _INFLAMED():
	def __init__(self,): 
		self.name = "INFLAMED"
		self.definitions = [u'(of a part of the body) red, painful, and swollen, especially because of infection: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
