

#calss header
class _AFFLUENT():
	def __init__(self,): 
		self.name = "AFFLUENT"
		self.definitions = [u'having a lot of money or owning a lot of things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
