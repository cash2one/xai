

#calss header
class _OPPRESSIVE():
	def __init__(self,): 
		self.name = "OPPRESSIVE"
		self.definitions = [u'cruel and unfair: ', u'causing people to feel worried and uncomfortable: ', u'If the weather or heat is oppressive, it is too hot and there is no wind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
