

#calss header
class _STRINGENT():
	def __init__(self,): 
		self.name = "STRINGENT"
		self.definitions = [u'having a very severe effect, or being extremely limiting: ', u'involving not enough money being available for borrowing as a result of firm controls on the amount of money in an economy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
