

#calss header
class _AERIAL():
	def __init__(self,): 
		self.name = "AERIAL"
		self.definitions = [u'in or from the air, especially from an aircraft: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
