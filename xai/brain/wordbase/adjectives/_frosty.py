

#calss header
class _FROSTY():
	def __init__(self,): 
		self.name = "FROSTY"
		self.definitions = [u'very cold, with a thin layer of white ice covering everything: ', u"If someone, or someone's behaviour, is frosty, they are unfriendly and not welcoming: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
