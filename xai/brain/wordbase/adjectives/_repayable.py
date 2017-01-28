

#calss header
class _REPAYABLE():
	def __init__(self,): 
		self.name = "REPAYABLE"
		self.definitions = [u'If something is repayable, you must pay it back: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
