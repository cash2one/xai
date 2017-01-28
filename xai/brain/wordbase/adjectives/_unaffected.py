

#calss header
class _UNAFFECTED():
	def __init__(self,): 
		self.name = "UNAFFECTED"
		self.definitions = [u'not influenced, harmed, or interrupted in any way: ', u'natural and sincere in your behaviour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
