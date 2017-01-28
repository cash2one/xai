

#calss header
class _HUMPBACKED():
	def __init__(self,): 
		self.name = "HUMPBACKED"
		self.definitions = [u'(of an animal) having a round raised part on its back: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
