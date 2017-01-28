

#calss header
class _DUCTILE():
	def __init__(self,): 
		self.name = "DUCTILE"
		self.definitions = [u'A ductile metal can be bent easily.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
