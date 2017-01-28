

#calss header
class _PSYCHIC():
	def __init__(self,): 
		self.name = "PSYCHIC"
		self.definitions = [u'having a special mental ability, for example so that you are able to know what will happen in the future or know what people are thinking: ', u'(especially of an illness) of the mind rather than the body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
