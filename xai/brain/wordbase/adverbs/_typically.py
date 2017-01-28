

#calss header
class _TYPICALLY():
	def __init__(self,): 
		self.name = "TYPICALLY"
		self.definitions = [u'in a way that shows all the characteristics that you would expect from the stated person, thing, or group: ', u'used when you are giving an average or usual example of a particular thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
