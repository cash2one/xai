

#calss header
class _LONG():
	def __init__(self,): 
		self.name = "LONG"
		self.definitions = [u'used to mean "(for) a long time", especially in questions and negative sentences: ', u'a long period of time before or after something: ', u'used with the past participle or the -ing form of the verb to mean that a state or activity has continued for a long time: ', u'used to say that something must happen before something else can happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
