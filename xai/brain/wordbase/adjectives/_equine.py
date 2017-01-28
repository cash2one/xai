

#calss header
class _EQUINE():
	def __init__(self,): 
		self.name = "EQUINE"
		self.definitions = [u'connected with horses, or appearing similar to a horse: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
