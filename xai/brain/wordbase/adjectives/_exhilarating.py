

#calss header
class _EXHILARATING():
	def __init__(self,): 
		self.name = "EXHILARATING"
		self.definitions = [u'making you feel very excited and happy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
