

#calss header
class _PIZZICATO():
	def __init__(self,): 
		self.name = "PIZZICATO"
		self.definitions = [u'played by plucking the strings of a musical instrument such as a violin or cello with the fingers instead of using a bow']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
