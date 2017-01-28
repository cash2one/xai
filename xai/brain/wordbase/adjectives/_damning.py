

#calss header
class _DAMNING():
	def __init__(self,): 
		self.name = "DAMNING"
		self.definitions = [u'A damning report, judgment, remark, etc. that includes a lot of criticism or shows clearly that someone is wrong, guilty, or has behaved very badly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
