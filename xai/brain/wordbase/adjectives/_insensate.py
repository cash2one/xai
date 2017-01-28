

#calss header
class _INSENSATE():
	def __init__(self,): 
		self.name = "INSENSATE"
		self.definitions = [u'not aware of what you are doing or what is happening around you: ', u"not feeling any sympathy for other people's suffering: ", u'having none of the characteristics of life that an animal or plant has: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
