

#calss header
class _VIRGIN():
	def __init__(self,): 
		self.name = "VIRGIN"
		self.definitions = [u'A virgin forest or area of land has not yet been cultivated (= used to grow crops) or used by people: ', u'Virgin oil, especially olive oil, is made directly from pressing the fruit, rather than by using heat: ', u'pure and not spoiled, especially when describing something white: ', u'never having had sex: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
