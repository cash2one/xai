

#calss header
class _SURREALISTIC():
	def __init__(self,): 
		self.name = "SURREALISTIC"
		self.definitions = [u'not seeming real; very unusual or impossible']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
