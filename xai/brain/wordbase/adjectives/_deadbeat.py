

#calss header
class _DEADBEAT():
	def __init__(self,): 
		self.name = "DEADBEAT"
		self.definitions = [u'not willing to pay debts or accept responsibilities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
