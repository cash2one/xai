

#calss header
class _OVERAGE():
	def __init__(self,): 
		self.name = "OVERAGE"
		self.definitions = [u'older than a particular age and therefore no longer allowed to do or have particular things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
