

#calss header
class _DESERVED():
	def __init__(self,): 
		self.name = "DESERVED"
		self.definitions = [u'used to refer to something that you earn or are given because of your behaviour or qualities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
