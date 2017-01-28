

#calss header
class _TAWNY():
	def __init__(self,): 
		self.name = "TAWNY"
		self.definitions = [u'of a light yellowish-brown colour, like that of a lion']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
