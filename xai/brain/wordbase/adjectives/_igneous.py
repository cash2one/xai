

#calss header
class _IGNEOUS():
	def __init__(self,): 
		self.name = "IGNEOUS"
		self.definitions = [u'(of rocks) formed from magma (= very hot liquid rock that has cooled)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
