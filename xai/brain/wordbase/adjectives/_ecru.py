

#calss header
class _ECRU():
	def __init__(self,): 
		self.name = "ECRU"
		self.definitions = [u'having a pale brown or cream colour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
