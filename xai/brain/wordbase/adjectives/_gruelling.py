

#calss header
class _GRUELLING():
	def __init__(self,): 
		self.name = "GRUELLING"
		self.definitions = [u'extremely tiring and difficult, and demanding great effort and determination: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
