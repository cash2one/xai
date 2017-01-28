

#calss header
class _UNACCENTED():
	def __init__(self,): 
		self.name = "UNACCENTED"
		self.definitions = [u'spoken without any accent (= the way people from a particular country or area pronounce words): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
