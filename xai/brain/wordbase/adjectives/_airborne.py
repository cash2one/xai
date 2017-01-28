

#calss header
class _AIRBORNE():
	def __init__(self,): 
		self.name = "AIRBORNE"
		self.definitions = [u'in the air, or carried by air or wind or by an aircraft: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
