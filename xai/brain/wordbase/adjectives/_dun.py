

#calss header
class _DUN():
	def __init__(self,): 
		self.name = "DUN"
		self.definitions = [u'of a greyish-brown colour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
