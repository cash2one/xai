

#calss header
class _SNUG():
	def __init__(self,): 
		self.name = "SNUG"
		self.definitions = [u'(of a person) feeling warm, comfortable, and protected, or (of a place, especially a small place) giving feelings of warmth, comfort, and protection: ', u'fitting closely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
