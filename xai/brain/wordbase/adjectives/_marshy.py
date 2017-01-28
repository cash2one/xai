

#calss header
class _MARSHY():
	def __init__(self,): 
		self.name = "MARSHY"
		self.definitions = [u'A marshy area of land is always wet, like a marsh: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
