

#calss header
class _CONTRACTILE():
	def __init__(self,): 
		self.name = "CONTRACTILE"
		self.definitions = [u'used to refer to body tissue that is able to contract, or to something that causes this to happen']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
