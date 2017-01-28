

#calss header
class _THEREBY():
	def __init__(self,): 
		self.name = "THEREBY"
		self.definitions = [u'as a result of this action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
