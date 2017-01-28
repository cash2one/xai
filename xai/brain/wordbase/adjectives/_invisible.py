

#calss header
class _INVISIBLE():
	def __init__(self,): 
		self.name = "INVISIBLE"
		self.definitions = [u'impossible to see: ', u"used to refer to money that is added to a country's economy by activities such as the service and financial industries rather than the production of goods in factories: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
