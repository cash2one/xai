

#calss header
class _COLOURED():
	def __init__(self,): 
		self.name = "COLOURED"
		self.definitions = [u'having or producing a colour or colours: ', u'used to describe a person who has black or brown skin. This word is now considered offensive by most people: ', u'in South Africa, used to describe a person of mixed race: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
