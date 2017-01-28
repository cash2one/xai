

#calss header
class _INVIOLABLE():
	def __init__(self,): 
		self.name = "INVIOLABLE"
		self.definitions = [u'that must be respected and not removed or ignored: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
