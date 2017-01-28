

#calss header
class _FISCAL():
	def __init__(self,): 
		self.name = "FISCAL"
		self.definitions = [u'connected with (public) money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
