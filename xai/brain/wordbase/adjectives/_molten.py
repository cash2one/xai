

#calss header
class _MOLTEN():
	def __init__(self,): 
		self.name = "MOLTEN"
		self.definitions = [u'Molten metal or rock is in a liquid state because of great heat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
