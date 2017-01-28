

#calss header
class _TOGETHER():
	def __init__(self,): 
		self.name = "TOGETHER"
		self.definitions = [u'organized, confident of your abilities, and able to use them to achieve what you want: ', u'to get something organized: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
