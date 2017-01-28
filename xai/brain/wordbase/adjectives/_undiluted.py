

#calss header
class _UNDILUTED():
	def __init__(self,): 
		self.name = "UNDILUTED"
		self.definitions = [u'If a liquid is undiluted it has not been mixed with water to make it less strong.', u'If the truth or a fact, etc. is undiluted it is stated in a simple, clear way, without trying to disguise it or make it easier to accept.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
