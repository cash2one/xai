

#calss header
class _WILLOWY():
	def __init__(self,): 
		self.name = "WILLOWY"
		self.definitions = [u'(especially of a woman) graceful (= moving smoothly and attractively) and thin: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
