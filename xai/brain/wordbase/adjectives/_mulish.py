

#calss header
class _MULISH():
	def __init__(self,): 
		self.name = "MULISH"
		self.definitions = [u'A mulish person is very determined and refuses to change their plans for anyone else.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
