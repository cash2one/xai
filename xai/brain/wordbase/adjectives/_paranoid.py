

#calss header
class _PARANOID():
	def __init__(self,): 
		self.name = "PARANOID"
		self.definitions = [u'feeling extremely nervous and worried because you believe that other people do not like you or are trying to harm you: ', u'suffering from a mental illness in which you believe that other people are trying to harm you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
