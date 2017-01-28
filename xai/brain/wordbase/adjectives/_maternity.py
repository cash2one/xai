

#calss header
class _MATERNITY():
	def __init__(self,): 
		self.name = "MATERNITY"
		self.definitions = [u'related to pregnancy and birth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
