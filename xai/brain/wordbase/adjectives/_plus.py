

#calss header
class _PLUS():
	def __init__(self,): 
		self.name = "PLUS"
		self.definitions = [u'A plus number or amount is more than zero: ', u'more than the number or amount mentioned: ', u'used by teachers after a letter, such as B or C, to show that the standard of a piece of work is slightly higher than the stated mark: ', u'used to describe an advantage or good quality that something has: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
