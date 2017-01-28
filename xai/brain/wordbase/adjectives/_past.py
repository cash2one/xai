

#calss header
class _PAST():
	def __init__(self,): 
		self.name = "PAST"
		self.definitions = [u'used to refer to a period of time before and until the present: ', u'having happened or existed before now: ', u'finished: ', u'of the past tense: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
