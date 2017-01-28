

#calss header
class _QUITE():
	def __init__(self,): 
		self.name = "QUITE"
		self.definitions = [u'completely: ', u'used to express that you are not certain about something: ', u"used to show agreement with someone's opinion: ", u'used to emphasize the degree or amount of something, or to say that someone or something is impressive, interesting, or unusual: ', u'used for emphasis: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
