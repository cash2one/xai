

#calss header
class _BUTCH():
	def __init__(self,): 
		self.name = "BUTCH"
		self.definitions = [u'(of a woman) looking or behaving like a man, or (of a man) being very strong with big muscles, and behaving in a traditionally male way']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
