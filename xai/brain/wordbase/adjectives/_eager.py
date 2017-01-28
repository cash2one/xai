

#calss header
class _EAGER():
	def __init__(self,): 
		self.name = "EAGER"
		self.definitions = [u'wanting very much to do or have something, especially something interesting or enjoyable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
