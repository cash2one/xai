

#calss header
class _NORMATIVE():
	def __init__(self,): 
		self.name = "NORMATIVE"
		self.definitions = [u'relating to rules, or making people obey rules, especially rules of behaviour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
