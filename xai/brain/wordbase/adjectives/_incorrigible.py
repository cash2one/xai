

#calss header
class _INCORRIGIBLE():
	def __init__(self,): 
		self.name = "INCORRIGIBLE"
		self.definitions = [u'An incorrigible person or incorrigible behaviour is bad and impossible to change or improve: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
