

#calss header
class _FREE():
	def __init__(self,): 
		self.name = "FREE"
		self.definitions = [u'not limited or controlled: ', u'relaxed and informal: ', u'costing nothing, or not needing to be paid for: ', u'not a prisoner any longer, or having unlimited movement: ', u'not in a fixed position or not joined to anything: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
