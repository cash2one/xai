

#calss header
class _SECURE():
	def __init__(self,): 
		self.name = "SECURE"
		self.definitions = [u'positioned or fixed firmly and correctly and therefore not likely to move, fall, or break: ', u'A secure place is one that it is difficult to get out of or escape from: ', u'likely to continue and not fail or be lost: ', u'(especially of objects, situations, etc.) able to avoid being harmed by any risk, danger, or threat: ', u'not doubting or being worried about yourself and your personal relationships: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
