

#calss header
class _SEROUS():
	def __init__(self,): 
		self.name = "SEROUS"
		self.definitions = [u'relating to serum (= the clear, watery part of any liquid in the body): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
