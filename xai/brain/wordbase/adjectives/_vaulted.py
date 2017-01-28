

#calss header
class _VAULTED():
	def __init__(self,): 
		self.name = "VAULTED"
		self.definitions = [u'related to or having a vault: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
