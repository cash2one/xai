

#calss header
class _EARLY():
	def __init__(self,): 
		self.name = "EARLY"
		self.definitions = [u'near the beginning of a period of time, or before the usual, expected, or planned time: ', u'Early flowers and vegetables are ones that are ready early in the year, before most other ones.', u'used after a date or time to show that something will not happen before then: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
