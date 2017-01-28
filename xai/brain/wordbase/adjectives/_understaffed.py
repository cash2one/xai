

#calss header
class _UNDERSTAFFED():
	def __init__(self,): 
		self.name = "UNDERSTAFFED"
		self.definitions = [u'If a shop, business, or organization is understaffed, it does not have enough employees: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
