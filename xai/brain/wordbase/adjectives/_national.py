

#calss header
class _NATIONAL():
	def __init__(self,): 
		self.name = "NATIONAL"
		self.definitions = [u'relating to or typical of a whole country and its people, rather than to part of that country or to other countries: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
