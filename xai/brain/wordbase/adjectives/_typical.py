

#calss header
class _TYPICAL():
	def __init__(self,): 
		self.name = "TYPICAL"
		self.definitions = [u'showing all the characteristics that you would usually expect from a particular group of things: ', u'showing all the bad characteristics that you expect from someone or something, often in a way that is annoying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
