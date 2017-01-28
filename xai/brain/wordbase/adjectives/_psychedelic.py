

#calss header
class _PSYCHEDELIC():
	def __init__(self,): 
		self.name = "PSYCHEDELIC"
		self.definitions = [u'(of a drug) causing effects on the mind, such as feelings of deep understanding or unusually strong experiences of colour , sound, taste, and touch : ', u'Psychedelic art or clothing has bright colours and strange patterns of a type that might be experienced by taking psychedelic drugs.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
