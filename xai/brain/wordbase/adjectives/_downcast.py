

#calss header
class _DOWNCAST():
	def __init__(self,): 
		self.name = "DOWNCAST"
		self.definitions = [u'sad and without hope: ', u"If someone's eyes are downcast, they are looking down."]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
