

#calss header
class _PHLEGMATIC():
	def __init__(self,): 
		self.name = "PHLEGMATIC"
		self.definitions = [u'A phlegmatic person does not usually get emotional or excited about things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
