

#calss header
class _AWOL():
	def __init__(self,): 
		self.name = "AWOL"
		self.definitions = [u'abbreviation for absent without leave: used to say that a member of the armed forces is away without permission: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
