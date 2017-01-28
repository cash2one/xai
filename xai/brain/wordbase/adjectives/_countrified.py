

#calss header
class _COUNTRIFIED():
	def __init__(self,): 
		self.name = "COUNTRIFIED"
		self.definitions = [u'A countrified person or thing belongs to or is suited to the countryside: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
