

#calss header
class _SCATHING():
	def __init__(self,): 
		self.name = "SCATHING"
		self.definitions = [u'criticizing someone or something in a severe and unkind way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
