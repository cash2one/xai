

#calss header
class _BOMBASTIC():
	def __init__(self,): 
		self.name = "BOMBASTIC"
		self.definitions = [u'using long and difficult words, usually to make people think you know more than you do: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
