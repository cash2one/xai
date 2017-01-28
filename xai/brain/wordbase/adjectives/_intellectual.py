

#calss header
class _INTELLECTUAL():
	def __init__(self,): 
		self.name = "INTELLECTUAL"
		self.definitions = [u'relating to your ability to think and understand things, especially complicated ideas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
