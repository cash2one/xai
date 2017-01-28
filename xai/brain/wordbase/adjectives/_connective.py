

#calss header
class _CONNECTIVE():
	def __init__(self,): 
		self.name = "CONNECTIVE"
		self.definitions = [u'connecting: ', u'Connective structures in the body connect different parts.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
