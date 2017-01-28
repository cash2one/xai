

#calss header
class _OUTGOING():
	def __init__(self,): 
		self.name = "OUTGOING"
		self.definitions = [u'(of a person) friendly and energetic and finding it easy and enjoyable to be with others: ', u'leaving a place, or leaving a job: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
