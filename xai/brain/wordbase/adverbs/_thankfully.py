

#calss header
class _THANKFULLY():
	def __init__(self,): 
		self.name = "THANKFULLY"
		self.definitions = [u'used, usually at the beginning of a sentence, to show you are happy or grateful about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
