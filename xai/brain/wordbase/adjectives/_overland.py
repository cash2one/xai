

#calss header
class _OVERLAND():
	def __init__(self,): 
		self.name = "OVERLAND"
		self.definitions = [u'(of travel) across the land in a vehicle, on foot, or on a horse; not by sea or air: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
