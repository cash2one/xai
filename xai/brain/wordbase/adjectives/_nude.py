

#calss header
class _NUDE():
	def __init__(self,): 
		self.name = "NUDE"
		self.definitions = [u'not wearing any clothes: ', u'being the colour of skin: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
