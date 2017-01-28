

#calss header
class _PRESUMPTUOUS():
	def __init__(self,): 
		self.name = "PRESUMPTUOUS"
		self.definitions = [u'A person who is presumptuous shows little respect for others by doing things they have no right to do: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
