

#calss header
class _PREDOMINANT():
	def __init__(self,): 
		self.name = "PREDOMINANT"
		self.definitions = [u'more noticeable or important, or larger in number, than others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
