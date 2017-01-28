

#calss header
class _NATURALLY():
	def __init__(self,): 
		self.name = "NATURALLY"
		self.definitions = [u'happening or existing as part of nature and not made or done by people: ', u'having an ability or characteristic from birth: ', u'If a particular skill comes naturally (to you), you are able to do it easily, with little effort or learning: ', u'as you would expect: ', u'in a normal way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
