

#calss header
class _FESTIVE():
	def __init__(self,): 
		self.name = "FESTIVE"
		self.definitions = [u'having or producing happy and enjoyable feelings suitable for a festival or other special occasion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
