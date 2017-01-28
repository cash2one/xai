

#calss header
class _JEALOUS():
	def __init__(self,): 
		self.name = "JEALOUS"
		self.definitions = [u'upset and angry because someone that you love seems interested in another person: ', u'unhappy and angry because someone has something that you want: ', u'extremely careful in protecting someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
