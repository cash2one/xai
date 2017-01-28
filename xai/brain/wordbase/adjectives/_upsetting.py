

#calss header
class _UPSETTING():
	def __init__(self,): 
		self.name = "UPSETTING"
		self.definitions = [u'making someone feel worried, unhappy, or angry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
