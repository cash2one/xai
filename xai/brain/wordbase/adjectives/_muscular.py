

#calss header
class _MUSCULAR():
	def __init__(self,): 
		self.name = "MUSCULAR"
		self.definitions = [u'related to muscles: ', u'having well-developed muscles: ', u'powerful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
