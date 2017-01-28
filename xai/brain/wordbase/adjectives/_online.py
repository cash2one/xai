

#calss header
class _ONLINE():
	def __init__(self,): 
		self.name = "ONLINE"
		self.definitions = [u'Online products, services, or information can be bought or used on the internet: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
