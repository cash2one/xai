

#calss header
class _STICKY():
	def __init__(self,): 
		self.name = "STICKY"
		self.definitions = [u'made of or covered with a substance that stays attached to any surface it touches: ', u'If the weather is sticky, it is very hot and the air feels wet.', u'difficult: ', u'unwilling to agree: ', u'used to describe a website or shop where people like to spend a long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
