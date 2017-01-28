

#calss header
class _ECONOMICALLY():
	def __init__(self,): 
		self.name = "ECONOMICALLY"
		self.definitions = [u'using little money, time, etc.: ', u"in a way that relates to a country's trade, industry, and money: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
